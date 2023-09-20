from setuptools import find_packages, setup

VERSION = "1.0.0"

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="secristo",
    version=VERSION,
    packages=find_packages(),
    author="Samuel Boamah",
    author_email="samboamah@icloud.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    install_requires=["cryptography>=3.4.7", "typer>=0.4.0"],
    entry_points={
        "console_scripts": [
            "secristo=secristo.cli:main",
        ],
    },
    keywords=[
        "secristo",
        "encryptor",
        "file encryptor",
        "folder encryptor",
        "encryption",
        "decryption",
        "fernet",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
