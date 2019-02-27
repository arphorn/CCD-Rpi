
from tkinter import*
from PIL import ImageTk, Image
import THSP
root = Tk()

Spinbox = Spinbox(root,from_=0,to = 1)
Spinbox.grid(row=5, column=3)


root.title("Test Termarind :)( ")
root.geometry('680x500')

  


def start(event):
   s = Spinbox.get()
 
   if ( s == "1"):
      THSP.process()
      imglabel = Label(root, image=img).grid(row=2, column=1)
   elif (s == "0"):
      print('lasca')
   
  
       



#img = ImageTk.PhotoImage(Image.open("save_pic_thsp/correlation00.png"))



button_Start = Button(root,text=" Set strat ")
button_Start.bind("<Button-1>", start)
button_Start.grid(row = 1, column = 1)












root.mainloop()
