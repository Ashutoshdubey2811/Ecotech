from setuptools import find_packages, 
from typing import List

def get_requirements(file_path: str) -> List[str]:
    
    #This function will return the list of requirements
    
    requirements = []
    with open(file_path) as file_obj:
        requirements =  file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    return requirements

setup(
    name="",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here, e.g. 'numpy', 'pandas'
    ],
    author="Ashutosh Dubey",
    author_email="itzykhan@gmail.com",
    description="This package id used basically for the learning purposse and completing the Internship assignments",
    url="https://github.com/Ashutoshdubey2811/Ecotech.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires= get_requirements('requirement.txt'),
)

