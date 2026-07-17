from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = "-e ."
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, "r") as file:
        requirements.extend([line.strip() for line in file.readlines() if line.strip() and line.strip() != hyphen_e_dot])
    if hyphen_e_dot in requirements:
        requirements.remove(hyphen_e_dot)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Victoria",
    author_email="victoria.palecek@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)