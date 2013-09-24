#!/usr/bin/env python
'''
Author : Bhavyanshu Parasher
Email : bhavyanshu@codershangout.org
Description : zBzOCR is a GUI tool written in python which helps extract text from images. It is based on the tesseract-ocr engine.
'''

from PIL import *
from Tkinter import *
from ttk import *
import tkFileDialog 
import sys
try:
	import Image
	from tesseract import image_to_string
except ImportError:
    raise ImportError,"The Tesseract module is required to run this program"


#Button actions for Master Window


def openhelp(event=None):
	print "Help!"




#Top Menu bar functions
def onExit(event=None):
        quit()

def loadFile():
      
        ftypes = [('Supported Image files', '*.png'), ('All files', '*')]
        dlg = tkFileDialog.Open(filetypes = ftypes)
        fl = dlg.show()
        
        if fl != '':
            content=image_to_string(Image.open(fl))
	    '''Create a Text widget'''
	    txt = Text()
	    txt.pack(fill=BOTH, expand=1)
            txt.insert(END, content)

