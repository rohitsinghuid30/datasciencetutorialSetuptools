from setuptools import find_packages, setup
from typing import List



# function of requirements.txt
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return List of requirements 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('/n', "") for req in requirements]
    return requirements



setup(
    name="SetupTools tutorial",
    version="0.0.1",
    description="This setuptools explore how to use in your code.",
    author="Rohit Singh",
    author_email="rohituid30@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)