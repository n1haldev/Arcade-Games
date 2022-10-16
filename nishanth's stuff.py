from tkinter import *
from nish import *
'''def call_and_destroy(x=0):
    root.destroy()
    TTT.Gameon()'''
root=Tk()
l=Label(root,text="hello boi")
l.pack()
b1=Button(root,text="Lol what a joke",command=lambda:fun(l))
b1.pack()
mainloop()
