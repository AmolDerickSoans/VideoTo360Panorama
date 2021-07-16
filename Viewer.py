import tkinter as tk
import tkinter.ttk as ttk
import webbrowser,os
import threading
import PIL.ImageTk
import PIL.Image
import glob
import shutil
from tkinter import *
from tkinter import filedialog
from opencv360 import FrameBreaker,makeCollageAble,collage,process,panorama


LARGEFONT =("Verdana", 35)

class app(tk.Tk):
    
    def __init__(self,*args,**kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self) 
       
        #container.pack(side = "top",  expand = True)
        container.grid(column=1,row=1)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (StartPage, Page1, Page2):
  
            frame = F(container, self )
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
           
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

      
        ##filewin = Toplevel(self)
        ##button = Button(filewin, text="Do nothing button")
        ##button.pack()
        
        #favicon
        
        #making a menuBar for future use
       
        
        #TITLE
        #titleimage
        logo = PIL.Image.open(fp="resources/360-camera.png")
        logo = logo.resize((80 ,80),PIL.Image.ANTIALIAS)
        logoPlace = PIL.ImageTk.PhotoImage(logo)
        label1 = Label(image=logoPlace)
        label1.image = logoPlace 
        label1.grid(column=1,row=0,padx=10,pady=10)
        #Title Text

        Title = Label(self, text = 'openCV360 v1.04')
        Title.config(font=("Courier",14))
        Title.grid(column=0,row=1,padx=30,pady=10)
        

        Filename = ""
        #FILE Operations
        #Vid 1
        def browseFiles1():
            filename = filedialog.askopenfilename(initialdir = "/" , title = "Select a VideoFile", filetypes = (("VideoFiles","*.mp4"),("all files","*.*")))
            Vid1Name.insert(END,filename)
            browseFiles1.Video1Path = Vid1Name.get()



        File1Prompt = Label(self, text = 'Choose Video 1')
       
        File1Prompt.grid(column=0,row=3,padx=10,pady=10)
        button_chooseVid1 = ttk.Button(self, text = "Browse Files" , command = browseFiles1)
        Vid1Name = ttk.Entry(self , width = 50)
       
        Vid1Name.grid(column=0,row=4,padx=10,pady=10)

        button_chooseVid1.grid(column=1,row=4,padx=10,pady=10)



        #Vid2
        def browseFiles2():
            filename = filedialog.askopenfilename(initialdir = "/" , title = "Select a VideoFile", filetypes = (("VideoFiles","*.mp4"),("all files","*.*")))
            Vid2Name.insert(END,filename)
            browseFiles2.Video2Path = Vid2Name.get()

        File2Prompt = Label(self, text = 'Choose Video 2')
      
        File2Prompt.grid(column=0,row=5,padx=10,pady=10)
        button_chooseVid2 = ttk.Button(self, text = "Browse Files" , command = browseFiles2)
        Vid2Name = ttk.Entry(self , width = 50)
      
        Vid2Name.grid(column=0,row=6,padx=10,pady=10)

        button_chooseVid2.grid(column=1,row=6,padx=10,pady=10)


        #vid3

        def browseFiles3():
            filename = filedialog.askopenfilename(initialdir = "/" , title = "Select a VideoFile", filetypes = (("VideoFiles","*.mp4"),("all files","*.*")))
            Vid3Name.insert(END,filename)
            browseFiles3.Video3Path = Vid3Name.get()

        File3Prompt = Label(self, text = 'Choose Video 3')
    
        File3Prompt.grid(column=0,row=7,padx=10,pady=10)
        button_chooseVid3 = ttk.Button(self, text = "Browse Files" , command = browseFiles3)
        Vid3Name = ttk.Entry(self , width = 50)
       
        Vid3Name.grid(column=0,row=8,padx=10,pady=10)

        button_chooseVid3.grid(column=1,row=8,padx=10,pady=10)



        #slider to set frame skip
        v1 = DoubleVar()


        def show1():  
            
            sel = "Frames to Be Skipped = " + str(v1.get())
            SelectedFrameSkipLabel.config(text = sel, font =("Courier", 9))  
        
        
        FrameSlider = Scale( self, variable = v1, 
                from_ = 5, to = 100, 
                orient = HORIZONTAL ,length= 190)   
    
        FrameSlider.grid(column=0,row=10,padx=10,pady=5)
        
        FrameSliderLabel = Label(self, text = "Frame Skipper")
     
        FrameSliderLabel.grid(column=0,row=9,padx=10,pady=10)
        SelectedFrameSkipLabel = Label(self)
    
        SelectedFrameSkipLabel.grid(column=0,row=11,padx=10,pady=10)
        

        SetFrameSkipButton = ttk.Button(self, text = 'SET', command = show1)
        
        SetFrameSkipButton.grid(column=1,row=10,padx=10,pady=5)

        ##vid length warning

        def getFrames():
            skip = v1.get()
            print(int(skip)) 
            ### Single Thread ###
            """ FrameBreaker.frameBreaker(browseFiles1.Video1Path , "output/vid1" , skip, "a" , "Vid1")
            FrameBreaker.frameBreaker(browseFiles2.Video2Path , "output/vid2" , skip, "b" , "vid2")
            FrameBreaker.frameBreaker(browseFiles3.Video3Path , "output/vid3" , skip, "c" , "vid3")
            delete_blurred("output/vid1")
            delete_blurred("output/vid2")
            delete_blurred("output/vid3") """
            ####Multithreading the frame split function####
            th1 = threading.Thread(target= FrameBreaker.frameBreaker, args=(browseFiles1.Video1Path , "output/vid1" , skip, "a" , "Vid1"))
            th1.start()
            th2 = threading.Thread(target= FrameBreaker.frameBreaker , args=(browseFiles2.Video2Path , "output/vid2" , skip, "b" , "vid2"))
            th2.start()
            th3 = threading.Thread(target= FrameBreaker.frameBreaker,args=(browseFiles3.Video3Path , "output/vid3" , skip, "c" , "vid3"))
            th3.start()
            
            
            
            ##Space to write loading function in mainThread

            th1.join()
            th2.join()
            th3.join()
            """ th4 = threading.Thread(target= process.delete_blurred, args=( "output/vid1",))
            th4.start()
            th5 = threading.Thread(target= process.delete_blurred, args=( "output/vid2",))
            th5.start()
            th6 = threading.Thread(target= process.delete_blurred, args=( "output/vid3",))
            th6.start()
            th4.join()
            th5.join()
            th6.join()  """
            process.delete_blurred("output/vid1")
            process.delete_blurred("output/vid2")
            process.delete_blurred("output/vid3")
            """  makeCollageAble.collageAble("output/vid1", "output/collage1/")
            makeCollageAble.collageAble("output/vid2", "output/collage2/")
            makeCollageAble.collageAble("output/vid3", "output/collage3/")
            collage.collageMaker("output/collage1",1)
            collage.collageMaker("output/collage2",2)
            collage.collageMaker("output/collage3",3) """
            print("completed")
            button_next['state'] = NORMAL

            


        button_run = ttk.Button(self,text = "RUN" ,command = getFrames)

        button_run.grid(column=0,row=12,padx=5,pady=10)
        button_next = ttk.Button(self,text = "NEXT" , command = lambda : controller.show_frame(Page1)  ,state= NORMAL) #DISABLED#NORMAL
        
        button_next.grid(column=1,row=12,padx=5,pady=10)
       
          
  
  
# second window frame page1
class Page1(tk.Frame):
    
     
    def __init__(self, parent, controller):
       
            
        
        tk.Frame.__init__(self, parent)
        
        style = ttk.Style(self)
        style.configure('lefttab.TNotebook', tabposition='wn')   
        #img1 = PIL.ImageTk.PhotoImage(PIL.Image.open("output\collage1\FinalCollage.jpg"))
        tabControl = ttk.Notebook(self , style='lefttab.TNotebook')
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tab4 = ttk.Frame(tabControl)

        tabControl.add(tab1, text ='Video 1')
        tabControl.add(tab2, text ='video 2')
        tabControl.add(tab3, text ='Video 3')
        tabControl.add(tab4, text ='Confirm')
        tabControl.pack(expand = 1, fill ="both")

        def fullpath(Path):
            current = os.path.abspath(os.getcwd())
            Fullpath = str(current) + Path
            return Fullpath
        

        def openfolder(Path):
            current = os.path.abspath(os.getcwd())
            fullpath= str(current) + Path
            print(fullpath)
            os.startfile(fullpath)  
            
    
        def createFinalDir(): 
            for imgfile in os.scandir("output/final"):
                    os.remove(imgfile.path)

            print("creating final directory")
            dst_dir = "output/final"

            for file in glob.glob('output/vid*/*'):    
                if file.endswith(".jpg"): 
                    shutil.copy(file, dst_dir)
                

        
        def stitchSIFT():
            createFinalDir()
            print("stitching")
            panorama.PanoramaSIFT()
           
       
        
        #tab1
        ttk.Label(tab1,text = "Details and Preview extracted frames from Video 1"
                
                 ).grid(column = 0, 
                                    row = 0,
                                    padx = 3,
                       
                                    pady = 3)  
        
        canvas1 = Canvas(tab1 , width =360,height=120)
        """ img1 = PIL.ImageTk.PhotoImage(PIL.Image.open("output\collage1\FinalCollage.jpg"))
        canvas1.grid(column= 0,row=1 ,padx=5,pady=5)
        canvas1.create_image(0,0,anchor=NW , image = img1)  """
        
       
        
        button_view = ttk.Button(tab1,text ="View Images" , command = lambda: openfolder("\\output\\vid1"), 
        )
        button_view.grid(
            column= 0 , 
            row= 2,
            padx= 5,
            pady= 5
        )
        


        #tab2

        ttk.Label(tab2,

                text ="Details of Video 2").grid(column = 0,
                                            row = 0, 
                                            padx = 3,
                                            pady = 3)
        canvas2 = Canvas(tab2 , width =360,height=120,bg = 'black')
        canvas2.grid(column= 0,row=1 ,padx=5,pady=5)
        #img2 = PIL.ImageTk.PhotoImage(PIL.Image.open(fullpath("\output\collage2\FinalCollage.jpg")))
        #canvas2.create_image(0,0,anchor=NW , image = img2)
        ttk.Button(tab2,text ="View Images" , command = lambda: openfolder("\\output\\vid2"), 
        ).grid(
            column= 0 , 
            row= 2,
            padx= 5,
            pady= 5
        )

        #tab3

        ttk.Label(tab3,

                text ="Details of Video 3").grid(column = 0,
                                            row = 0, 
                                            padx = 3,
                                            pady = 3)
        canvas3 = Canvas(tab3 , width =360,height=120,bg = 'black')
        canvas3.grid(column= 0,row=1 ,padx=5,pady=5)
        #img3 = PIL.ImageTk.PhotoImage(PIL.Image.open(fullpath("\output\collage3\FinalCollage.jpg")))
        #canvas3.create_image(0,0,anchor=NW , image = img3)
        ttk.Button(tab3,text ="View Images" , command = lambda: openfolder("\\output\\vid3"), 
        ).grid(
            column= 0 , 
            row= 2,
            padx= 5,
            pady= 5
        )

        #tab4

        button_previousp1= ttk.Button(self, text =" << Previous",
                            command = lambda : controller.show_frame(StartPage)).pack() #grid(column = 4,row = 1,padx=5,pady=5)
        
        button_stitch= ttk.Button(self, text ="Stitch",
                            command = lambda : stitchSIFT()).pack()#grid(column = 5,row = 1,padx=20,pady=5)

        button_nextp1= ttk.Button(self, text ="Next >>",
                            command = lambda : controller.show_frame(Page2) ,state = DISABLED).pack()#grid(column = 6,row = 1,padx=20,pady=5)


   
  
  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
# Driver Code
app = app()
def donothing():
            print("blah")
menubar = Menu(app)
#fileMenu with options New ,Open ,Save ,SaveAs , Close
filemenu = Menu(menubar,tearoff =0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=app.quit)
menubar.add_cascade(label="File", menu=filemenu)
#help menu with links to github ,about(ppl who worked on openCV360 ) and paper
helpmenu = Menu(menubar, tearoff=0)

new = 1
url ="https://github.com/AmolDerickSoans/VideoTo360Panorama"
def openweb():
    webbrowser.open(url,new = new)


helpmenu.add_command(label="Github", command=openweb)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

app.config(menu=menubar)
app.iconbitmap(r'resources/favicon.ico')
app.title('OpenCV 360 V1.12')
#qapp.geometry("500x600+100+20")
app.mainloop()
