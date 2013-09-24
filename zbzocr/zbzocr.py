
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
	
	helpbutton = Button(self, text="Help", command=openhelp).pack(side=TOP, expand=YES, pady=2, anchor=N)
	



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
	helpMenu.add_command(label='README', underline=0)
	helpMenu.add_command(label='About', underline=0)
	



def main():
  
    root = Tk()
    root.option_readfile('zbzocr/optionDB')
    root.geometry("800x600")
    app = MainGUI(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
