#!/usr/bin/env python
'''
Author : Bhavyanshu Parasher
Email : bhavyanshu@codershangout.org
Description : zBzOCR is a GUI tool written in python which helps extract text from images. It is based on the tesseract-ocr engine.
'''
from PIL import *
from Tkinter import *
from ttk import *
from allUIfunctions import *
import sys
try:
	import Image
	from tesseract import image_to_string
except ImportError:
    raise ImportError,"The Tesseract module is required to run this program"
import os
import Tkinter as tk

'''Initializing splashscreen'''

root = tk.Tk()
# show no frame
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))
# take a .jpg picture you like, add text with a program like PhotoFiltre
# (free from http://www.photofiltre.com) and save as a .gif image file
image_file = os.path.join(os.path.dirname(__file__), 'splash.gif')
#assert os.path.exists(image_file)
# use Tkinter's PhotoImage for .gif files
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*0.8, width=width*0.8, bg="white")
canvas.create_image(width*0.8/2, height*0.8/2, image=image)
canvas.pack()
# show the splash screen for 5000 milliseconds then destroy
root.after(5000, root.destroy)
root.mainloop()


class MainGUI(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("zBzOCR - Extract Text from Images!")
        self.pack(fill=BOTH, expand=1)
        
        Style().configure("TFrame", background="#666", foreground="#FFF")
        
	
	labelhome = Label(self, text="Tip: To start importing, go to File>Import>Image",background="#666", foreground="#FFF").pack(side=TOP, expand=YES, pady=10) #label for home screen

	'''Button stack for home screen'''
	
        # Exit button
	exit_image = os.path.join(os.path.dirname(__file__), 'exit.gif')
        self.image = tk.PhotoImage(file=exit_image)
        self.ne = tk.Button(self, height=20,width=20,image=self.image, command=onExit)
        # ... and using place as the geometry manager
        self.ne.place(relx=1.0, rely=0.0, anchor="ne")



	'''Top menu bar'''
	
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
	helpMenu = Menu(menubar)
	
	#File Menu
	fileMenu = Menu(menubar)
        submenu1 = Menu(fileMenu)
        submenu1.add_command(label="Image",command=loadFile)
        fileMenu.add_cascade(label='Import', menu=submenu1, underline=0)
	fileMenu.add_separator()        
        fileMenu.add_command(label="Exit", underline=0, command=onExit)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)	

	#Help Menu
	helpMenu = Menu(menubar)
	submenu2 = Menu(helpMenu)
	submenu2.add_command(label="Help")
	menubar.add_cascade(label="Help", underline=0, menu=helpMenu)
	helpMenu.add_command(label='README', underline=0, command=openhelp)
	helpMenu.add_command(label='About', underline=0)
	


def main():
    root = Tk()	
    root.option_readfile(os.path.join(os.path.dirname(__file__), 'optionDB')) #Made file path OS independent
    root.overrideredirect(True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))
    #root.geometry("800x600")
    app = MainGUI(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
