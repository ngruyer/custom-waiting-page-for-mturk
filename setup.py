import os
import re
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

def read_version():
    with open('otree_mturk_utils/__init__.py', 'r') as f:
        version_match = re.search(
            r"^__version__ = ['\"]([^'\"]*)['\"]",
            f.read(), re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='mturkotreeutils',
    version=read_version(),
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='set of utilities for oTree and mTurk',
    long_description=README,
    url='https://github.com/chapkovski/custom-waiting-page-for-mturk',
    author='Essi Kujansuu - Nicolas Gruyer/Economics Games - Philipp Chapkovski',
    author_email='chapkovski@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django==1.8.8',
        'otree-core>=1.4.6',
        'django-radiogrid'
    ]
)