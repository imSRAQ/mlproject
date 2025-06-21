from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirement(file_path)->List[str]:
    """
        This function is used to read the requirement from the file
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name = "ML_project",
    version="0.0.0",
    author="SRAQ",
    author_email="rizwanquadri8899@gmail.com",
    packages = find_packages(),
    install_requires = get_requirement('requirements.txt'),
    
)