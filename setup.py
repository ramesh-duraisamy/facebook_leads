from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in facebook_leads/__init__.py
from facebook_leads import __version__ as version

setup(
	name="facebook_leads",
	version=version,
	description="Integrate Leads from FaceBook Lead Ads to Leads Doctype in ERPNext.",
	author="Raino",
	author_email="raino@tridotstech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
