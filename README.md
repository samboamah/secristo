# secristo

A Python CLI package that provides functionality to encrypt and decrypt files or folders using symmetric encryption.

## Features

- Encrypt a file or folder
- Decrypt a file or folder
- Uses the Fernet encryption algorithm from the `cryptography` library in Python

## Installation

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

Note: When prompted, enter the encryption key. The same key should be used for encryption and decryption. 
Make sure to store encryption keys very safely. 

Caution: The encryption key entered will not be diplayed on the interface. 