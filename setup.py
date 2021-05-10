from setuptools import setup

APP = ["main.py"]
DATA_FILES = [] #"photos/"]
OPTIONS = {
    "iconfile": "logo.icns",
    "argv_emulation": True,
    # "packages": ["certifi"],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)


# run /usr/local/bin/python3 /Users/jeandtx/Documents/Projet-transverse/setup.py py2app