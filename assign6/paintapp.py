from tkinter import *
from tkinter import ttk
import tkinter.filedialog
import tkinter.colorchooser
import PIL
from PIL import ImageGrab


class main:
    def __init__(self,master):
        self.master = master # Used in tkinter to specify it is the parent window
        self.color_fg = 'black' #Default pen colour
        self.color_bg = 'white' #Default background
        self.old_x = None #Initial x position of mouse
        self.old_y = None #Initial y position of mouse
        self.penwidth = 5 # Pen width 
        self.drawWidgets() # Function for drawing widgets
        self.c.bind('<B1-Motion>',self.paint) #Button 1 of the mouse will be used for drawing.
        self.c.bind('<ButtonRelease-1>',self.reset) #Button 1 of mouse is released.

    def paint(self,e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)
            #create_line(initial x,initial y,new x,new y,width,colour of line,capstyle denotes how the ends of the line look,smooth tells series of the lines:either parabolic or straight 

        self.old_x = e.x #x , y gives position of mouse
        self.old_y = e.y

    def reset(self,e):
        self.old_x = None
        self.old_y = None    #Not initialising to a random point for mouse after clearing canvas  

    def changeW(self,e):
        self.penwidth = e #To change the pen width

    def save(self):
        file = tkinter.filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*.png')]) #save in png format
        if file:
            x = self.master.winfo_rootx() + self.c.winfo_x()  #winfo_x() returns x coordinate from the upper left corner winfo_rootx() returns the left edge
            y = self.master.winfo_rooty() + self.c.winfo_y()  #winfo_y() returns y coordinate from the upper left corner winfo_rooty() returns the left edge 
            x1 = x + self.c.winfo_width()  #final x coordinate
            y1 = y + self.c.winfo_height() #final y coordinate

            PIL.ImageGrab.grab().crop((x,y,x1,y1)).save(file + '.png') #saves the file by taking a screeshot 
            
           

    def clear(self):
        self.c.delete(ALL)  #clear canvas

    def change_fg(self):
        self.color_fg=tkinter.colorchooser.askcolor(color=self.color_fg)[1]  #change the pen colour

    def change_bg(self):
        self.color_bg=tkinter.colorchooser.askcolor(color=self.color_bg)[1]  #change the background colour
        self.c['bg'] = self.color_bg

    def drawWidgets(self):
        self.controls = Frame(self.master,padx = 5,pady = 5) # sets the length and breadth of the window 
        Label(self.controls, text='Pen Width: ',font=('',15)).grid(row=0,column=0) # gives details of the Pen Width
        self.slider = ttk.Scale(self.controls,from_= 5, to = 100, command=self.changeW,orient=VERTICAL) # gives details of the scrollbar,increase pen width
        self.slider.set(self.penwidth) #set the penwidth
        self.slider.grid(row=0,column=1,ipadx=30) 
        self.controls.pack() #organizes the widget before putting them in parent widget
        
        self.c = Canvas(self.master,width=800,height=500,bg=self.color_bg)# defining the height ,width ,bg color 
        self.c.pack(fill=BOTH,expand=True) # expands to fill any space not otherwise used in widget's parent.
        # Determines whether widget fills any extra space allocated to it by the packer, or keeps its own minimal dimensions

        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='File..',menu=filemenu)#Hierarchial menu
        filemenu.add_command(label='Save..',command=self.save) #Save option
        colormenu = Menu(menu) 
        menu.add_cascade(label='Colors',menu=colormenu) #Color menu
        colormenu.add_command(label='Brush Color',command=self.change_fg)
        colormenu.add_command(label='Background Color',command=self.change_bg)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Options',menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas',command=self.clear)
        optionmenu.add_command(label='Exit',command=self.master.destroy) 
        
        

if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('DrawingApp')
    root.mainloop() # infinite loop, used when ready to run the code, waits for an event 