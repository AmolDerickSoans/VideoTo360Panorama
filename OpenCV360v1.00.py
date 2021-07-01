import tkinter 
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as pyplot
from PIL import ImageTk, Image  
import cv2

from opencv360 import FrameBreaker

root =Tk()

root.title('OpenCV 360 V1.00')
root.geometry("600x600+100+20")
#dummyfunction
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
#favicon
root.iconbitmap(r'resources/favicon.ico')
#making a menuBar for future use
menubar = Menu(root)
#fileMenu with options New ,Open ,Save ,SaveAs , Close
filemenu = Menu(menubar,tearoff =0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
#help menu with links to github ,about(ppl who worked on openCV360 ) and paper
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Github", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
#TITLE
#titleimage
logo = Image.open("resources/360-camera.png")
logo = logo.resize((80 ,80),Image.ANTIALIAS)
logoPlace = ImageTk.PhotoImage(logo)
label1 = tkinter.Label(image=logoPlace)
label1.image = logoPlace
label1.place(x=260, y=20)
#Title Text

Title = Label(root, text = 'openCV360 v1.00')
Title.config(font=("Courier",14))
Title.place(x=212 , y = 120)

Filename = ""
#FILE Operations
#Vid 1
def browseFiles1():
   filename = filedialog.askopenfilename(initialdir = "/" , title = "Select a VideoFile", filetypes = (("VideoFiles","*.mp4"),("all files","*.*")))
   Vid1Name.insert(END,filename)

File1Prompt = Label(root, text = 'Choose Video 1')
File1Prompt.place(x = 15 , y = 145)
button_chooseVid1 = Button(root, text = "Browse Files" , command = browseFiles1)
Vid1Name = Entry(root , width = 50)
Vid1Name.place(x =15 , y = 165)

button_chooseVid1.place(x = 330 , y = 158)
Video1Path = Vid1Name.get()

#Vid2
def browseFiles2():
   filename = filedialog.askopenfilename(initialdir = "/" , title = "Select a VideoFile", filetypes = (("VideoFiles","*.mp4"),("all files","*.*")))
   Vid2Name.insert(END,filename)

File2Prompt = Label(root, text = 'Choose Video 2')
File2Prompt.place(x = 15 , y = 245)
button_chooseVid2 = Button(root, text = "Browse Files" , command = browseFiles2)
Vid2Name = Entry(root , width = 50)
Vid2Name.place(x =15 , y = 265)

button_chooseVid2.place(x = 330 , y = 258)
Video2Path = Vid2Name.get()

#vid3

def browseFiles3():
   filename = filedialog.askopenfilename(initialdir = "/" , title = "Select a VideoFile", filetypes = (("VideoFiles","*.mp4"),("all files","*.*")))
   Vid3Name.insert(END,filename)

File3Prompt = Label(root, text = 'Choose Video 3')
File3Prompt.place(x = 15 , y = 345)
button_chooseVid3 = Button(root, text = "Browse Files" , command = browseFiles3)
Vid3Name = Entry(root , width = 50)
Vid3Name.place(x =15 , y = 365)

button_chooseVid3.place(x = 330 , y = 358)
Video3Path = Vid3Name.get()


#slider to set frame skip
v1 = DoubleVar()
def show1():  
      
    sel = "Frames to Be Skipped = " + str(v1.get())
    SelectedFrameSkipLabel.config(text = sel, font =("Courier", 9))  
  
  
FrameSlider = Scale( root, variable = v1, 
           from_ = 5, to = 100, 
           orient = HORIZONTAL)   
FrameSlider.place(x=25 , y= 430)
  
FrameSliderLabel = Label(root, text = "Frame Skipper")
FrameSliderLabel.place(x =15 ,y = 400)
SelectedFrameSkipLabel = Label(root)
SelectedFrameSkipLabel.place(x = 15  ,y= 470)

SetFrameSkipButton = Button(root, text = 'SET', command = show1)
SetFrameSkipButton.place(x= 200, y= 440 )

root.mainloop() 