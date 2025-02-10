from setuptools import setup, find_packages

setup(
    name="pyspace",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    author="Anonymous",
    author_email="anonymous@example.com",
    description="A brief description of the package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/magicalElectronicSpace/pyspace",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
