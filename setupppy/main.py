import os
import argparse
from pathlib import Path
from setupppy.Logger import logger
from setupppy.utils import (setup_py_template ,
                            requirements_txt_template ,
                            constants_init_template ,
                            help_text ,
                            src_init_template)

def welcome():
    print('SetUpppy: Your Project, Perfectly Structured!')

def help():
    print(help_text)

def create_folder_structure(project_name):
        
    list_of_files = [
        ".github/workflows/.gitkeep",
        f"src/{project_name}/__init__.py",

        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/components/data_ingestion.py",
        f"src/{project_name}/components/prepare_base_model.py",
        f"src/{project_name}/components/prepare_callbacks.py",
        f"src/{project_name}/components/training.py",
        f"src/{project_name}/components/evaluation.py",

        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/utils/common.py",

        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",

        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/pipeline/data_ingestion.py",
        f"src/{project_name}/pipeline/prepare_base_model.py",
        f"src/{project_name}/pipeline/training.py",
        f"src/{project_name}/pipeline/evaluation.py",
        f"src/{project_name}/pipeline/predict.py",

        f"src/{project_name}/entity/__init__.py",
        f"src/{project_name}/entity/config_intity.py",

        f"src/{project_name}/constants/__init__.py",

        "config/config.yaml",
        "dvc.yaml",
        "params.yaml",
        "requirements.txt",
        "setup.py",
        "research/trials.ipynb",
        "templates/index.html"
    ]

    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logger.info(f"Creating directory; {filedir} for the file: {filename}")

        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            with open(filepath, 'w') as f:
                if filename == '__init__.py' and filedir == f"src/{project_name}":
                    f.write(src_init_template)
                elif filename == 'setup.py':
                    f.write(setup_py_template)
                elif filename == 'requirements.txt':
                    f.write(requirements_txt_template)
                elif filename == '__init__.py' and 'constants' in filedir:
                    f.write(constants_init_template)
                else:
                    pass
                logger.info(f"Creating empty file: {filepath}")

        else:
            logger.info(f"{filename} already exists")

    print(f"Project structure for '{project_name}' created successfully.")

def main():
    parser = argparse.ArgumentParser(description='Create a folder structure for an ML project.')
    parser.add_argument('-n', '--name', type=str, help='Name of the project')
    parser.add_argument('command', nargs='?', default='setup', choices=['setup', 'help'], help='Command to run')

    args = parser.parse_args()

    if args.command == 'help':
        help()
    elif args.name:
        create_folder_structure(args.name)
    else:
        print("Error: The following arguments are required: -n/--name")
        parser.print_help()

if __name__ == '__main__':
    main()