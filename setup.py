import setuptools

with open("README.md","r") as fh:
	long_description = fh.read()

setuptools.setup(
    name="pysheeter",
    version="1.0.6",
    author="VicW",
    author_email="victor.vesterlund@gmail.com",
    description="Lightweight Python-script to create sprite sheets from transparent PNGs with Pillow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VictorWesterlund/pysheeter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=[
        "Pillow",
    ],
    python_requires='>=3.6',
)