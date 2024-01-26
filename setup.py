from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
print(get_requirements.__doc__)
setup(
name='mlproject',
version='1.0',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)

