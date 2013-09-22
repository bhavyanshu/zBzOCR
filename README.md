zBzOCR
======


#INSTALLATION & USAGE

##WINDOWS :
Python 2.7.5

1. Download & install (Any one of the below). Don't forget to add it to your path after installation. Example: Enter in Command prompt PATH=C:\Python27

http://www.python.org/ftp/python/2.7.5/python-2.7.5.msi
http://www.python.org/ftp/python/2.7.5/python-2.7.5.amd64.msi

2. You might need setuptools as well. So go on and download it from below link.
https://pypi.python.org/pypi/setuptools/1.1.6
Now open CLI and cd into setuptools extracted directory. Then run *python setup.py install*. It will install setuptools for you.

3. Once done, you have all that is required to install and run the program. 
Now simply cd into the directory and run *python setup.py install*. It will install my python program in your system. Once done, type in CLI *python ocr-gui.py* and have fun :)

##LINUX :


1. apt-get install tesseract-ocr. You must have tesseract CLI in your system. It is in the package list for debian. Not sure about the rest. You can find the installation note here http://code.google.com/p/tesseract-ocr/source/browse/tags/release-3.02.02/INSTALL

2. If you are running linux, then you might already be having complete python package in your system. If you want to check if you have python, then run in terminal *which python*. If you don't have, then you need to install python 2.7.X in your linux machine. 

3. Then you need to cd into the directory of my program and run *python setup.py install*. It will install my program in your linux machine. Now to use the program, simply issue *python ocr-gui.py*.
