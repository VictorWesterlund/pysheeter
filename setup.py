from setuptools import setup, find_packages

setup(
    name = "pysheeter",
    version = "1.1.0",
    description = "Simple python library for creating sprite sheets from images",
    author = "Victor Westerlund",
    author_email = "victor.vesterlund@gmail.com",
    url = "https://github.com/victorwesterlund/reflect-client-python",
    packages = ["pysheeter"],
    # The requirement.txt file should also be updated when changing this
    install_requires = ["pillow"]
)