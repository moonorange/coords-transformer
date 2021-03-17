from setuptools import find_packages, setup
from codecs import open
from os import path

package_name = "coordinates-transformer"

root_dir = path.abspath(path.dirname(__file__))

def _requirements():
    return [name.rstrip() for name in open(path.join(root_dir, 'requirements.txt')).readlines()]

def _dev_requirements():
    return [name.rstrip() for name in open(path.join(root_dir, 'requirements-dev.txt')).readlines()]

def get_version():
    version_filepath = path.join(path.dirname(__file__), package_name, 'version.py')
    with open(version_filepath) as f:
        for line in f:
            if line.startswith('__version__'):
                return line.strip().split()[-1][1:-1]

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=package_name,
    packages=[package_name],
    version=get_version(),
    license='MIT',
    install_requires=_requirements(),
    install_requires_dev=_dev_requirements(),
	author='tsurutan',
    author_email='tsurutan.android@gmail.com',
	maintainer='Sagri',
    maintainer_email='corporate@sagri.tokyo',
    url='https://github.com/sagri-tokyo/coordinates-transformer',
    description='Transform pixel coordinates to tile coordinates',
    long_description=long_description,
    keywords='tile, coordinates, pixel',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8'
    ],
)
