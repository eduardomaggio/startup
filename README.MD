# startup

Generates the initial project structure
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## How to use

First step is to create a file with the project information.
For example:

```project_info.txt```
```buildoutcfg
NAME=example
YEAR=2017
VERSION=0.1
DESCRIPTION=The example project short description
URL=http://example.com/repo
AUTHOR=SNOW, John
LICENSE=MIT
PACKAGES=['numpy', 'scipy']
ZIP_SAFE=FALSE
```

Then, run the script to generate all the directory structure of a project
```commandline
# python startup.py <project_info> [<path>]
python startup.py project_info.txt ../..
```
It will create the project structure
```commandline
LICENSE
Makefile
MANIFEST.in
README.MD
requirements.txt
setup.py
example/__init__.py
example/example.py
docs/
tests/
```
## Authors
* **MAGGIO, Eduardo**
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details 
## Acknowledgments
Thanks, God!
