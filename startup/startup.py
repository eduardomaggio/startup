# -------------------------------------------------------------------------------
# Name:        startup
# Purpose:     Generates the initial project structure
#
# Author:      MAGGIO, Eduardo
#
# Created:     06-10-2017
# Copyright:   (c) 2017 MAGGIO, Eduardo
# Licence:     MIT
# -------------------------------------------------------------------------------


import sys
import os
import datetime


def generate_readme(project, destination):
    filename = destination + "/README.MD"
    print(filename)
    with open(filename, "w") as f:
        name = project["NAME"]
        f.write("# " + name)
        f.write("\n\n")
        f.write(project["DESCRIPTION"])
        f.write("\n")
        f.write("## Getting Started\n")
        f.write("These instructions will get you a copy of the project up"
                " and running on your local machine for development and testing"
                " purposes. See deployment for notes on how to deploy the project"
                " on a live system.\n")
        packages = eval(project["PACKAGES"])
        if len(packages) != 0:
            f.write("### Prerequisites\n\n")
            f.write("Packages you need to install the software and how to install them\n")
            for pack in packages:
                f.write("\n```\n")
                f.write("# " + pack + "\n")
                f.write(" pip install " + pack + "\n")
                f.write("```\n")
            f.write("\n")
        f.write("### Installing\n")
        f.write("How to have to get a development env running\n")
        f.write("\n```\n")
        f.write(" python setup.py install")
        f.write("\n```\n")
        f.write("## How to use\n")
        f.write("\n```\n")
        f.write(" import " + name + "\n")
        f.write("\n```\n")
        f.write("## Authors\n")
        f.write("* **" + project["AUTHOR"] + "**\n")
        f.write("## License\n")
        f.write("This project is licensed under the " + project["LICENSE"] + " License - see the [LICENSE](LICENSE) "
                                                                             "file for details \n")
        f.write("## Acknowledgments\n")
        f.write("Thanks, God!\n")
        f.close()
    pass


def get_project(filename):
    project = {}
    with open(filename, "r") as f:
        lines = f.read().split("\n")
        for line in lines:
            expr = line.split("=")
            if 2 == len(expr):
                project[expr[0]] = expr[1]
        f.close()
    return project


def create_directories(project: object, root: object) -> object:
    directory = root + "/" + project["NAME"]
    package_dir = directory + "/" + project["NAME"]
    if not os.path.exists(directory):
        os.makedirs(directory)
        os.makedirs(package_dir)
        os.makedirs(directory + "/docs")
        os.makedirs(directory + "/tests")
        open(package_dir + "/__init__.py", "w").close()
    return directory


def generate_license(project, directory):
    filename = directory + "/LICENSE"
    print(filename)
    if project["LICENSE"] == 'MIT':
        mit = open("MIT-LICENSE.template")
        mit_lic = mit.read()
        mit.close()
        mit_lic = mit_lic.format(YEAR=project["YEAR"], AUTHOR=project["AUTHOR"])
        with open(filename, "w") as f:
            f.write(mit_lic)
            f.close()


def generate_requirements(project, directory):
    packages = eval(project["PACKAGES"])
    filename = directory + "/requirements.txt"
    print(filename)
    with open(filename, "w") as f:
        for pack in packages:
            f.write(pack + "\n")
        f.close()
    pass


def generate_setup(project, directory):
    filename = directory + "/setup.py"
    print(filename)
    f = open("setup.py.template")
    setup = f.read().format(
        NAME=project["NAME"],
        VERSION=project["VERSION"],
        DESCRIPTION=project["DESCRIPTION"],
        AUTHOR=project["AUTHOR"],
        URL=project["URL"],
        PACKAGES=project["PACKAGES"]
    )
    f.close()
    with open(filename, "w") as f:
        f.write(setup)
        f.close()
    pass


def generate_module(project, directory):
    name = project["NAME"]
    filename = directory + "/" + name + "/" + name + ".py"
    print(filename)
    f = open("module.py.template")
    module = f.read().format(
        NAME=name,
        YEAR=project["YEAR"],
        DESCRIPTION=project["DESCRIPTION"],
        AUTHOR=project["AUTHOR"],
        LICENSE=project["LICENSE"],
        DATE=datetime.datetime.today().strftime('%d-%m-%Y')
    )
    f.close()
    with open(filename, "w") as f:
        f.write(module)
        f.close()
    pass


def generate_manifest(project: object, directory: object) -> object:
    filename = directory + "/MANIFEST.in"
    print(filename)
    with open(filename, "w") as f:
        f.write("include LICENSE\n")
        f.close()
    pass


def generate_makefile(project, directory):
    filename = directory + "/Makefile"
    print(filename)
    with open(filename, "w") as f:
        f.write("init:\n    pip install -r requirements.txt\n\n")
        f.write("test:\n    py.test tests\n\n")
        f.write(".PHONY:\n    init test\n\n")
        f.close()
    pass


def main(argv: object) -> object:
    if len(argv) >= 1:
        project = get_project(argv[0])
        root = ".."
        if len(argv) == 2:
            root = argv[1]
        directory = create_directories(project, root)
        if not os.path.isfile(directory + '/README.MD'):
            generate_readme(project, directory)
        if not os.path.isfile(directory + '/LICENSE'):
            generate_license(project, directory)
        if not os.path.isfile(directory + '/setup.py'):
            generate_setup(project, directory)
        if not os.path.isfile(directory + '/requirements.txt'):
            generate_requirements(project, directory)
        if not os.path.isfile(directory + '/MANIFEST.in'):
            generate_manifest(project, directory)
        if not os.path.isfile(directory + '/Makefile'):
            generate_makefile(project, directory)
        name = project["NAME"]
        if not os.path.isfile(directory + '/' + name + '/' + name + ".py"):
            generate_module(project, directory)
    else:
        print("Missing argument...")
        print("use:\npython generate.py <project_info> [<path>]")
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
