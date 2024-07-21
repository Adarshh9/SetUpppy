setup_py_template = """\
from setuptools import setup, find_packages

PROJECT_NAME = ''
VERSION = '0.0.1'
DESCRIPTION = ''
AUTHOR_NAME = ''
AUTHOR_MAIL = 'example@gmail.com'

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR_NAME,
    author_email=AUTHOR_MAIL,
    packages=find_packages(),
    install_requires=requirements,
    keywords=['python']
)
"""

requirements_txt_template = """\
setuptools
"""

constants_init_template = """\
from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")    
"""

src_init_template = """\
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir ,"running_logs.log")
os.makedirs(log_dir ,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("Logger")
"""

help_text = """\
Commands

    - `setup -n Project_Name`: Creates the project structure with the specified project name.
    - `setup help`: Prints this help documentation.
    - `setupppy`: Displays a special welcome message.
"""