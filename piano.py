from tkinter import *
from buzz import *

    


class PianoGUI:
    
    
    def __init__(self,master):
        self.master=master
        master.title("Piano Gui")
        self.Label=Label(master,text="Mid")
        self.Label.grid(row=0,columnspan=11)
        
        self.buttonc=Button(master,bg="white",text="C",command=lambda: self.sound_c(262),height=10,width=3)
        self.buttonc.grid(row=5,column=0)
        
        self.buttoncs=Button(master,bg="black",fg="white",text="C#",command=lambda: self.sound_c(277),height=10,width=2)
        self.buttoncs.grid(row=1,columnspan=2)
        
        self.buttonds=Button(master,bg="black",fg="white",text="D#",command=lambda: self.sound_c(311),height=10,width=2)
        self.buttonds.grid(row=1,columnspan=4)
        
        self.buttond=Button(master,bg="white",text="D",command=lambda: self.sound_c(294),height=10,width=3)
        self.buttond.grid(row=5,column=1)

        self.buttone=Button(master,bg="white",text="E",command=lambda: self.sound_c(330),height=10,width=3)
        self.buttone.grid(row=5,column=2)
        
        self.buttonf=Button(master,bg="white",text="F",command=lambda: self.sound_c(349),height=10,width=3)
        self.buttonf.grid(row=5,column=3)
        
        self.buttonfs=Button(master,bg="black",fg="white",text="F#",command=lambda: self.sound_c(370),height=10,width=2)
        self.buttonfs.grid(row=1,column=3,columnspan=2)
        
        self.buttong=Button(master,bg="white",text="G",command=lambda: self.sound_c(392),height=10,width=3)
        self.buttong.grid(row=5,column=4)
        
        self.buttongs=Button(master,bg="black",fg="white",text="G#",command=lambda: self.sound_c(415),height=10,width=2)
        self.buttongs.grid(row=1,column=4,columnspan=2)
        
        self.buttona=Button(master,bg="white",text="A",command=lambda: self.sound_c(440),height=10,width=3)
        self.buttona.grid(row=5,column=5)
        
        self.buttonas=Button(master,bg="black",fg="white",text="A#",command=lambda: self.sound_c(466),height=10,width=2)
        self.buttonas.grid(row=1,column=5,columnspan=2)
        
        self.buttonb=Button(master,bg="white",text="B",command=lambda: self.sound_c(494),height=10,width=3)
        self.buttonb.grid(row=5,column=6)
        self.buttonc5=Button(master,bg="white",text="C5",command=lambda: self.sound_c(523),height=10,width=3)
        self.buttonc5.grid(row=5,column=7)
    def sound_c(self,freq):
        play_c(freq)
        
root=Tk()
gui=PianoGUI(root)

root.mainloop()

        
    
