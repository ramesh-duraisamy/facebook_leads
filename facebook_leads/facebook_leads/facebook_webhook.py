import frappe

@frappe.whitelist(allow_guest = True)
def handleFaceBookWebhook():

	# Handling POST Request (Incoming Webhook Data)
	if frappe.request.method == "POST":
		data = frappe.request.data
		createLead(data)
		return "OK", 200
	
	# GET Request ( Verification and Setup of Webhook)
	elif frappe.request.method == "GET":

		from werkzeug.wrappers import Response
		response = Response()
		
		hub_mode = frappe.request.args.get("hub.mode")
		hub_challenge = frappe.request.args.get("hub.challenge")
		hub_verify_token = frappe.request.args.get("hub.verify_token")

		verify_token = frappe.db.get_single_value('FB Configuration','verify_token')

		if hub_mode == "subscribe" and hub_verify_token == verify_token:
			response.mimetype = "text/plain"
			response.data = hub_challenge
			return response
		else:
			frappe.response.status_code = 403
			return "Verification failed"
	else:
		return "Invalid request", 400

import json
import requests
@frappe.whitelist(allow_guest=True)
def createLead(data):
	try:
		dataDict = data.decode()
		finalData = json.loads(dataDict)
		# frappe.log_error("LeadGen Webhook Data",finalData)
		has_custom_fields = frappe.db.get_single_value('FB Configuration','has_custom_fields')
		company = frappe.db.get_single_value('FB Configuration','company')
		
		leadgen_id = finalData["entry"][0]["changes"][0]["value"]["leadgen_id"]
		page_id = finalData["entry"][0]["changes"][0]["value"]["page_id"]
		form_id = finalData["entry"][0]["changes"][0]["value"]["form_id"]
		ad_id = finalData["entry"][0]["changes"][0]["value"]["ad_id"]

		access_token = frappe.db.get_single_value('FB Configuration','access_token')
		lead_owner = frappe.db.get_single_value('FB Configuration','lead_owner')

		### API for Fetching FormData
		url=f"https://graph.facebook.com/v18.0/{leadgen_id}"
		fieldsList = json.dumps(["field_data","ad_name","campaign_id","campaign_name","platform"])
		r = requests.get(url = url, params = {"access_token":access_token,"fields":fieldsList})

		get_data=r.json()
		frappe.log_error("Lead Data",get_data)
		res_data=get_data["field_data"]
		ad_name = get_data["ad_name"]
		campaign_id = get_data["campaign_id"]
		campaign_name = get_data["campaign_name"]
		platform = get_data["platform"]


		### API to get Lead Form Name
		formNameURL=f"https://graph.facebook.com/v18.0/{form_id}"
		formNameReq = requests.get(url=formNameURL, params = {"access_token":access_token,"fields":["name"]})

		formNameData = formNameReq.json()
		resFormNameData = formNameData['name']
		# frappe.log_error('FormName',resFormNameData)

		formData={}

		for i in res_data:
			formData[i['name']]=i['values'][0]

		if has_custom_fields and company == 'Homegenie':

			custom_product_enquired= "Rocotile"
			company_name = "Homegenie Building Products Private Limited"

			if page_id == "2446209195462119":
				custom_product_enquired = 'Rocotile'
				company_name = 'Homegenie Building Products Private Limited'

			if page_id == "108012537277681":
				custom_product_enquired = 'Bioman'
				company_name = 'Bioman Sewage Solutions Private Limited'
			
			if page_id == "103617114844048":
				custom_product_enquired = "D'sign Doors"
				company_name = "Doortisan Creations Private Limited"
			
			if page_id == "109056373809678":
				custom_product_enquired = 'Timbe'
				company_name = 'Timbe Windows Private Limited'
			

			fbLeadData = f'Form Name : {resFormNameData}\n\n'

			for i in formData.items():
				fbLeadData += f'{i[0]} : {i[1]}\n'
			
			keysList = formData.keys()

		if has_custom_fields and company != 'Homegenie':
			company_name = company

		doc=frappe.new_doc("Lead")

		doc.first_name = formData['full_name'] if 'full_name' in keysList else 'Not Found'
		doc.email_id = formData['email'] if 'email' in keysList else ''
		mobile_no = formData['phone_number'] if 'phone_number' in keysList else ""

		if mobile_no != "":
			mobile_no = mobile_no.replace(' ','').replace('-','')
			if len(mobile_no) > 10:
				doc.mobile_no = mobile_no[3:]
			else:
				doc.mobile_no = mobile_no
				
		## WhatsApp Number
		if 'phone_number' in keysList:
			if len(mobile_no) > 10:
				whatsapp_no = mobile_no[3:]
			else:
				whatsapp_no = mobile_no
		elif 'whatsapp_no' in keysList:
			if len(formData['whatsapp_no']) > 10:
				whatsapp_no = formData['whatsapp_no'][3:]
			else:
				whatsapp_no = formData['whatsapp_no']
		else:
			whatsapp_no = ""

		doc.whatsapp_no = whatsapp_no.replace(' ','')
		doc.city = formData['city'] if 'city' in keysList else ""
		doc.company = company_name
		doc.owner = lead_owner

		if company == 'Homegenie':
			doc.status="Lead"
			doc.source="Facebook"
			doc.custom_product_enquired= custom_product_enquired
			doc.custom_customer_category="B2C"
			doc.type="Incoming"
			doc.custom_fb_lead_data = fbLeadData
			doc.custom_ads_id = ad_id
			doc.custom_ads_name = ad_name
			doc.custom_form_id = form_id
			doc.custom_form_name = resFormNameData
			doc.custom_campaign_id = campaign_id
			doc.custom_campaign_name = campaign_name
			doc.custom_platformsource = platform

		doc.insert(ignore_permissions = True,ignore_mandatory=True,ignore_links=True)
		frappe.db.commit()
	except:
		frappe.log_error('Lead Creation Failed',frappe.get_traceback())