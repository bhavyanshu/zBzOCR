#!/usr/bin/env python
'''
Author : Bhavyanshu Parasher
Email : bhavyanshu@codershangout.org
Description : zBzOCR is a GUI tool written in python which helps extract text from images. It is based on the tesseract-ocr engine.
'''

from PIL import *
from PIL import Image, ImageTk
from Tkinter import *
import Tkinter as tk
from ttk import *
import tkFileDialog 
import os
import sys
try:
	import Image
	from tesseract import image_to_string
except ImportError:
    raise ImportError,"The Tesseract module is required to run this program"


#Button actions for Master Window


def openhelp(event=None):
	myTextWidget= Text() # set up a text widget as a root (window)
	myFile = file(os.path.join(os.path.dirname(__file__), 'help.txt'))
	myText= myFile.read() # read the file to variable
	myFile.close() # close file handle
	myTextWidget.insert(0.0,myText) # insert the file's text into the text
	myTextWidget.pack(expand=1, fill=BOTH) # show the widget

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
	    loadImage(fl)

def loadImage(loadthisimage):
	NewWindow = Toplevel()
	NewWindow.title('Original Image')
	# load the file and covert it to a Tkinter image object
	image1 = ImageTk.PhotoImage(Image.open(loadthisimage))
	# get the image size
	w = image1.width()
	h = image1.height()
	# position coordinates of newwindow 'upper left corner'
	x = 0
	y = 0
	# make the toplevel window the size of the image
	NewWindow.geometry("%dx%d+%d+%d" % (w, h, x, y))
	Label(NewWindow, image=image1).pack()
	NewWindow.mainloop()  # start the GUI for newWindow
