#!/usr/bin/env python
'''
Author : Bhavyanshu Parasher
Email : bhavyanshu@codershangout.org
Description : This file contains all the main functions for the GUI.
'''
try:
	from easygui import *
except ImportError:
    raise ImportError,"The easygui module is required to run this program"

import sys
try:
	import Image
	from tesseract import image_to_string
except ImportError:
    raise ImportError,"The Tesseract module is required to run this program"



def AskForFile():
    fname = fileopenbox(msg='Filename: ', title='Please select the scanned document', default='*', filetypes= ["*.png", "*.jpg", "*.jpeg"]) 
    content=image_to_string(Image.open(fname))
    choices=['Copy to Clipboard','Wrong output? Try again!']
    textbox(msg='The following text was extracted from the image', title='Text', text=content, codebox=0)


def help(): # create a function called Dump
    msgbox("Author : Bhavyanshu Parasher (bhavyanshu@codershangout.org)","Help!")



def Post(): # create a function called Post
    f = open(fname, "a"); # open the file defined in Ask.
    message = enterbox(msg='Enter Message: ', title='Post', default=''); # Define message as the result of another enterbox.
    f.write("\n"); # write a newline to the file.
    f.write(message) # write your message to the file.


    
def Die(): # Define the function Die.
    sys.exit() # Quit The Program.

