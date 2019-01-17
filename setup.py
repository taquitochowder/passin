import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="passin",
    version="0.1",
    author="Thakee Chowdhury",
    author_email="thakeechow@gmail.com",
    description="A password generator/manager that does both at the same time.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/taquitochowder/passin",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['passin = passin.main:main']
    }
)
