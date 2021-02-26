from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as rf:
    requirements = rf.read().split()

setup(name='dpsutil216',
      version='1.0.0',
      description='This repository contain all util',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/connortran216/dpsutil216.git',
      author='ConnorTran',
      author_email='canhtran210699@gmail.com',
      packages=find_packages(),
      install_requires=requirements,
      python_requires='>=3.6')
