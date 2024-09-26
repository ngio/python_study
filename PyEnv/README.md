Simple Python Version Management: pyenv

https://github.com/pyenv/pyenv

## pyenv lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.

This project was forked from rbenv and ruby-build, and modified for Python.



![image](https://github.com/user-attachments/assets/6acc88ed-5206-482f-b397-43a37e90b216)


## What pyenv does...
* Lets you change the global Python version on a per-user basis.
* Provides support for per-project Python versions.
* Allows you to override the Python version with an environment variable.
* Searches for commands from multiple versions of Python at a time. This may be helpful to test across Python versions with tox.

## In contrast with pythonbrew and pythonz, pyenv does not...
* Depend on Python itself. pyenv was made from pure shell scripts. There is no bootstrap problem of Python.
* Need to be loaded into your shell. Instead, pyenv's shim approach works by adding a directory to your PATH.
* Manage virtualenv. Of course, you can create virtualenv yourself, or pyenv-virtualenv to automate the process.
