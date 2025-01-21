from setuptools import find_packages,setup
# setuptools is a Python library designed for packaging and distributing Python code
# setup: The main function provided by setuptools that is used to define the package metadata and configuration.
# find_packages: A utility function that automatically discovers all Python packages and sub-packages in the current directory (based on the presence of __init__.py files).

from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # the problem here is \n will also be read between each line in requirements.txt
        requirements = [req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    
    return requirements

'''
open(file_path): Opens the file specified by file_path.
file_obj.readlines(): Reads all the lines in the file into a list. Each line in the file becomes a string in the list
 e.g ['numpy\n', 'pandas\n', '-e .\n']

 -e . is a common entry in requirements.txt, indicating that the current project should be installed as a package in "editable mode."
 For many use cases (e.g., pip installation), this line is unnecessary.

 setup.py is mapped to requirements.txt using '-e .'

'''
setup(
    name = 'First ML Project',
    version='0.0.1',
    author='Subrat Bahuguna',
    author_email='bahuguna.subrat211996@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)


# important point here is we need a 2 way connection between setup.py and requirements.txt , i.e even if we seperately install using requirements.txt
# still the setup.py should get invoked to build the packages with the modifications, i.e any modification in requirements.txt should run setup.py as well
# for this '-e .' is used to connect between them
# also when opening requirements.txt , we should not read '-e .'