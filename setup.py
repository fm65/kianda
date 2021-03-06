#!/usr/bin/env python3

from distutils.core import setup


setup(
	name='kianda',
	version='1.0',
	description='Editor de texto do projeto dipanda',
    long_description=open('README.md').read(),
	author='Fidel R. Monteiro',
	py_modules= [
		"src/findwindow",
		"src/highlighter",
		"src/linenumbers",
		"src/statusbar",
		"src/textarea",
		"src/texteditor",
		"src/syntax",
        "src/config",
        "src/terminal",
        "src/interactiveConsole"
    ],
	entry_points = {
		"console_scripts": ["kianda = src.texteditor:main"]	
	},
    license="",
)
 
