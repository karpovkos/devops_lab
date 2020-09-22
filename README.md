DevOps Lab 2020 summer
# Created a simple, separate python app which would monitor your system/server.
=================

# Initialization
To install package run command `pip install wheel`

To build app with run command `python setup.py bdist_wheel`

# How 2 install app
To install app use `pip install .`

# How 2 run app
Run command to launch system monitor `snapshot -i <num> -t <str>`

**t** - `txt` or `json`  -- file format

**i** - snapshot interval

defaults: `t=txt` and `i=30`

# How 2 get help
Run command to get help `snapshot -h`

# How 2 remove app
Run command to uninstall app `pip uninstall snapshot`

