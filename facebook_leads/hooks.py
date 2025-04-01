from . import __version__ as app_version

app_name = "facebook_leads"
app_title = "Facebook Leads"
app_publisher = "Raino"
app_description = "Integrate Leads from FaceBook Lead Ads to Leads Doctype in ERPNext."
app_email = "raino@tridotstech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/facebook_leads/css/facebook_leads.css"
# app_include_js = "/assets/facebook_leads/js/facebook_leads.js"

# include js, css files in header of web template
# web_include_css = "/assets/facebook_leads/css/facebook_leads.css"
# web_include_js = "/assets/facebook_leads/js/facebook_leads.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "facebook_leads/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "facebook_leads.utils.jinja_methods",
#	"filters": "facebook_leads.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "facebook_leads.install.before_install"
# after_install = "facebook_leads.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "facebook_leads.uninstall.before_uninstall"
# after_uninstall = "facebook_leads.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "facebook_leads.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"facebook_leads.tasks.all"
#	],
#	"daily": [
#		"facebook_leads.tasks.daily"
#	],
#	"hourly": [
#		"facebook_leads.tasks.hourly"
#	],
#	"weekly": [
#		"facebook_leads.tasks.weekly"
#	],
#	"monthly": [
#		"facebook_leads.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "facebook_leads.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "facebook_leads.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "facebook_leads.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["facebook_leads.utils.before_request"]
# after_request = ["facebook_leads.utils.after_request"]

# Job Events
# ----------
# before_job = ["facebook_leads.utils.before_job"]
# after_job = ["facebook_leads.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"facebook_leads.auth.validate"
# ]
