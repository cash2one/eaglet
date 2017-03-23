from distutils.core import setup
import os

def fullsplit(path, result=None):
	"""
	Split a pathname into components (the opposite of os.path.join)
	in a platform-neutral way.
	"""
	if result is None:
		result = []
	head, tail = os.path.split(path)
	if head == '':
		return [tail] + result
	if head == path:
		return result
	return fullsplit(head, [tail] + result)

def is_package(package_name):
	return True

packages, package_data = [], {}

root_dir = os.path.dirname(__file__)
if root_dir != '':
	os.chdir(root_dir)
eaglet_dir = 'eaglet'

for dirpath, dirnames, filenames in os.walk(eaglet_dir):
	# Ignore PEP 3147 cache dirs and those whose names start with '.'
	dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != '__pycache__']
	parts = fullsplit(dirpath)
	package_name = '.'.join(parts)
	if '__init__.py' in filenames and is_package(package_name):
		packages.append(package_name)
	elif filenames:
		relative_path = []
		while '.'.join(parts) not in packages:
			relative_path.append(parts.pop())
		relative_path.reverse()
		path = os.path.join(*relative_path)
		#package_files = package_data.setdefault('.'.join(parts), [])
		#package_files.extend([os.path.join(path, f) for f in filenames])

print packages

setup(
	name='eaglet', 
	version='1.0.3',
	url='https://git2.weizzz.com:84/microservice/eaglet',
	author='weizoom microservice infrastructure team', 
	author_email='chenru@weizoom.com',
	packages=packages
)