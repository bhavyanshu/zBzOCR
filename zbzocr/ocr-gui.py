#!/usr/bin/env python
'''
Author : Bhavyanshu Parasher
Email : bhavyanshu@codershangout.org
Description : This is the main GUI call to the python based tesseract OCR engine. This is specifically designed for zBzQuiz PHP web API and will be used by professors to easily fetch text from scanned documents.
'''

from vars import *
try:
	from easygui import *
except ImportError:
    raise ImportError,"The easygui module is required to run this program"

try:
	import Image
	from tesseract import image_to_string
except ImportError:
    raise ImportError,"The Tesseract module is required to run this program"


msg = "What would you have me do, my lord?"
title = "zBzOCR - Extract text from images!"
choices=['Proceed to text extractor','View Help Document','Exit']


def Main(): # Define a function called Main, which is the main window of the program.

    choice = indexbox(msg, title, choices); # choose the function, Returns 0 for Post, 1 For Dump Etc.

    if  choice == 0: # If choice equals 0, then:

        AskForFile() # Run Ask.
        Main() # Return to the main window.
    
    elif choice == 1: # If the first if returns false, then check if choice equals 1, if so then:

        help() # Run dump.
        Main() # Return to the main window.
    
    elif choice == 2: # If the second if returns false, then check if choice equals 2, if so then:

        Die() # Run Die, which closes the program.
    
Main() # Run the Main window. ^ This was all one function remember.
