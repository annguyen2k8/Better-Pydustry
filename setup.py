from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pydustry",
    version="0.0.1",
    author="annguyen2k8",
    description="A module check info server mindustry.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/annguyen2k8/Better-Pydustry",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)