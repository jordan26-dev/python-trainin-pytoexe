import sys
import os
from cx_Freeze import setup, Executable

# ADD Files
files = ['resources/'] 

# TARGET
target = Executable(
    script="login_pyqt5.py",
    base="Win32GUI",
    icon="resources/images/cnx new logo.ico"
)

# SETUP CX_FREEZE
setup(
    name="UI App",
    version="1.0",
    description="app desc",
    author="author name",
    options = {'build.exe' : {'include_files' : files}},
    executables = [target]
)



