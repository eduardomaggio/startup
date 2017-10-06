

from setuptools import setup, find_packages


with open('README.MD') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='startup',
    version='0.1',
    description='Generates the initial project structure',
    long_description=readme,
    author='MAGGIO, Eduardo',
    url='http://',
    license=license,
    packages=[]
)

