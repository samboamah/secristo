# secristo

A Python CLI package that provides functionality to encrypt and decrypt files or folders using [symmetric encryption](https://www.sciencedirect.com/topics/computer-science/symmetric-encryption#:~:text=Symmetric%20encryption%20uses%20a%20single,kept%20secret%20from%20third%20parties.).

## Features

- Encrypt a file or folder
- Decrypt a file or folder
- Uses the [Fernet](https://www.comparitech.com/blog/information-security/what-is-fernet/) encryption algorithm from the [`cryptography`](https://pypi.org/project/cryptography/) library in Python

## Installation

Download the package to your local machine:
```shell
$ git clone https://github.com/samboamah/secristo.git
```

Install the package:
```shell
$ pip install secristo
```

## Usage

Encrypt a file:
```shell
$ secristo encrypt /path/to/file.txt
```

Encrypt a folder:
```shell
$ secristo encrypt /path/to/folder
```

Decrypt a file:
```shell
$ secristo decrypt /path/to/file.txt
```

Decrypt a folder:
```shell
$ secristo decrypt /path/to/folder
```

## Note

When prompted, enter the encryption key. The same key should be used for encryption and decryption. 
Make sure to store encryption keys very safely.
Encryption key entered will not be diplayed on the interface. 

## Author
[Samuel Boamah](https://github.com/samboamah)