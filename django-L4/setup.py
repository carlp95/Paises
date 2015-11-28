import os 
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__),'README.rst')) as readme:
	README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir)))

setup(
	name = 'django-L4',
	version = '0.1',
	packages = ['L4'],
	include_package_data = True,
	license = 'BSD License',
	description = 'Una simple aplicacion para mostrar paises.',
	long_description = README,
        url = 'http://www.tareapaisesL4.com/',
	author = 'Carlos Perez',
        author_email = 'carlosperezurena@gmail.com',
	classifiers = [
		'Enviroment :: Web Enviroment',
		'Framework :: Django',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operathing System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Topic :: Internet :: www/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	],
)
