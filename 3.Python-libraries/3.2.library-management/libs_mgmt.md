# Managing libraries in python

The most popular way of installing external packages in Python is by using pip. According to the author, pip is short for "pip installs packages", a recursive abbreviation.
It is a Python module that manages external Python packages.

## pip arguments

- _install_ : install new packages
- _--upgrade_ : upgrade existing packages to the latest version
- uninstall : remove the package from the system
- freeze : prints a list of all the installed packages (via pip) and their dependencies

## Usage

```
python3 -m pip install flask
```

(This is how pip is implemented and this command installs the library called flask)

## Installing from requirements.txt

```
[!bash!]$ cat requirements.txt

flask
click
```

```
[!bash!]$ python3 -m pip install -r requirements.txt
```

## Operators for specifying version of the library

- == : Version matching clause
- <= / >= : Inclusive ordered comparison clause
- < / > : Exclusive ordered comparison clause
  <br>

  For example, if we know that some package xyz is vulnerable to exploitation at versions 1.0.4 and lower, we can specify in our requirements file that we need xyz>=1.0.5.
