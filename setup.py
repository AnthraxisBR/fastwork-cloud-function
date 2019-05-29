
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='fastwork_cloud_function',
     version='0.1',
     scripts=['swfastwork'],
     author="Gabriel Mourão de Melo",
     author_email="gabrielmouraodemelo@gmail.com",
     description="A package to be used with Swoole FastWork (PAAS Unifier)",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/AnthraxisBR/fastwork-cloud-function",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )