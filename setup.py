from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="azdo-cli",
    version="1.0.1",
    author="Migz Estrella",
    author_email="me@migzestrella.com",
    description="An Azure DevOps CLI client.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/migzpogi/azdo-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
    [console_scripts]
    azdocli=azdocli.azdocli:cli
    ''',
)