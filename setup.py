from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj :
        requirements = file_obj.readlines()
        # print(requirements)
        # output: [' pandas\n', ' numpy\n', ' seaborn\n', ' matplotlib\n', ' ']
        requirements =[req.replace("\n","") for req in requirements]
        # print(requirements)
        # output: ['pandas', 'numpy', 'seaborn', 'matplotlib', '']
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ML projects',
    version='0.0.1',
    author='Abhoy',
    author_email='abhoy.ghosh2004@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)

 