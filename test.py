from tkinter import *  
import tkinter.ttk as ttk
from PIL import ImageTk,Image  
""" root = Tk()  
canvas = Canvas(root, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("output/collage1/FinalCollage.jpg"))  
canvas.create_image(0,0,anchor=NW, image=img) 
root.mainloop()  """
root = Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.pack(expand = 1, fill ="both")
  
ttk.Label(tab1, 
          text ="Welcome to \
          GeeksForGeeks").grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 30)  
canvas = Canvas(tab1, width = 300, height = 300)  
canvas.grid(column= 1, row =0)
img = ImageTk.PhotoImage(Image.open("output/collage1/FinalCollage.jpg"))  
canvas.create_image(0,0,anchor=NW, image=img) 
ttk.Label(tab2,
          text ="Lets dive into the\
          world of computers").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)
  
root.mainloop()  

