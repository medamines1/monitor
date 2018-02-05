import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'readme.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
	name= "django-monitor",
	version = "1.0",
	description = "A django app to monitor the traffic of  django instances with admin panel",
	author ="mohamed amine dahmen",
	author_email="m_amine22@outlook.fr",
	packages=find_packages(), 
	include_package_data=True,
	zip_safe=False,
	license='MIT License',
	long_description=README,

)