import setuptools

with open('readme.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_askasnr',   # this should be unique
	version = '0.0.1',
	author = 'Sam Aska',
	author_email = 'askasnr8@gmail.com',
	description = 'This is preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'Licence :: OSI Aproved :: MIT Licence',
	'Operating System :: OS Independent'],
	python_requires = '>=3.5'
	)