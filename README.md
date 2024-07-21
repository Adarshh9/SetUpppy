# SetUpppy

SetUpppy: Your Project, Perfectly Structured!

## Description

SetUpppy is a Python package that helps you create a standard folder structure for end-to-end machine learning projects. This tool aims to make project setup faster, easier, and more organized.

## Features

- Automatically create a project folder structure
- Includes necessary configuration files and scripts
- Easy to use command-line interface

## Installation

To install SetUpppy, use pip:

```bash
pip install setupppy
```

## Usage

### Command Line

Once installed, you can use the `setupppy` command to create a new project structure. Here's how you can do it:

1. Open your terminal.
2. Navigate to the directory where you want to create your project.
3. Run the following command:

```bash
setupppy -n Project_Name
```

Replace `Project_Name` with the desired name of your project.

### Example

To create a new project called `my_ml_project`, you would run:

```bash
setupppy -n my_ml_project
```

### Project Structure

After running the command, the following folder structure will be created:

```
.
├── .github
│   └── workflows
│       └── .gitkeep
├── config
│   └── config.yaml
├── dvc.yaml
├── params.yaml
├── requirements.txt
├── research
│   └── trials.ipynb
├── setup.py
├── src
│   └── my_ml_project
│       ├── __init__.py
│       ├── components
│       │   ├── __init__.py
│       │   ├── data_ingestion.py
│       │   ├── prepare_base_model.py
│       │   ├── prepare_callbacks.py
│       │   ├── training.py
│       │   └── evaluation.py
│       ├── utils
│       │   ├── __init__.py
│       │   └── common.py
│       ├── config
│       │   ├── __init__.py
│       │   └── configuration.py
│       ├── pipeline
│       │   ├── __init__.py
│       │   ├── data_ingestion.py
│       │   ├── prepare_base_model.py
│       │   ├── training.py
│       │   ├── evaluation.py
│       │   └── predict.py
│       ├── entity
│       │   ├── __init__.py
│       │   └── config_entity.py
│       └── constants
│           └── __init__.py
├── templates
│   └── index.html
└── logs
    └── running_logs.log
```

### Logging

SetUpppy includes a logging mechanism that logs the creation of directories and files. The logs are stored in `logs/running_logs.log`.

### Commands

    - `setup -n Project_Name`: Creates the project structure with the specified project name.
    - `setup help`: Prints this help documentation.
    - `setupppy`: Displays a special welcome message.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Author

Adarsh Kesharwani  
Email: akesherwani900@gmail.com

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
