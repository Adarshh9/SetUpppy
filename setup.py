from setuptools import setup ,find_packages

VERSION = '0.2'
DESCRIPTION = 'End To End Project Folder Structure Setup Tool'

with open('requirements.txt' ,'r') as f:
    requirements = f.read().splitlines()

with open('README.md' ,'r') as f:
    long_description = f.read()

setup(
    name='setupppy',
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Adarsh Kesharwani',
    author_email='akesherwani900@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
    keywords=['python','setup','mlops','end to end','project'],
    entry_points={
        "console_scripts":[
            "setupppy = setupppy:welcome",
            "setup = setupppy.main:main",
        ],
    },
)
