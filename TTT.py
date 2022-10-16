from tkinter import *
from tkinter.messagebox import showinfo

def Gameon():
    
    win=Tk()
    win.title("Tic-Tac-Toe")
    win.geometry("1500x1000")
    numbers=[1,2,3,4,5,6,7,8,9]
    # y='X' for player1 and 'O' for player2
    y=""
    # x is the counter to keep counting the number of chances
    x=0
    #boards is a list to store the mark with respect to the cell number
    boards=[""]*10
     
    def result(boards,mark):
        return ((boards[1] == boards[2] == boards [3] == mark) 
                or (boards[4] == boards[5] == boards [6] == mark) 
                or (boards[7] == boards[8] == boards [9] == mark) 
                or (boards[1] == boards[4] == boards [7] == mark) 
                or (boards[2] == boards[5] == boards [8] == mark)
                or (boards[3] == boards[6] == boards [9] == mark)
                or (boards[1] == boards[5] == boards [9] == mark) 
                or (boards[3] == boards[5] == boards [7] == mark))
                
    def decider(a,b,n):
            nonlocal x,y,numbers
            x,y,num=a,b,n
            if x%2==0:
                y='X'
                boards[num]=y
            elif x%2!=0:
                y='O'
                boards[num]=y
            lb[num-1].config(text=y) #Display X or O on the button clicked by user
            x=x+1
            mark=y
            # Here we are calling the result() to decide whether we have got the winner or not
            if(result(boards,mark) and mark=='X' ):
                #If Player1 is the winner show a dialog box stating the winner
                showinfo("Result","Player1 wins")
                #Call the destroy function to close the GUI
                destroys()
            elif(result(boards,mark) and mark=='O'):
                showinfo("Result","Player2 wins")
                destroys()
     
    def click(num):
        nonlocal x,y,numbers
        """ To Check which button has been clicked to avoid over-writing"""
        if num in numbers:
            numbers.remove(num)
            decider(x,y,num)
                 
        # If we have not got any winner, display match has been tied.
        if(x>8 and result(boards,'X')==False and result(boards,'O')==False):
            showinfo("Result","Match Tied")
            destroys()

    def destroys():
        # destroys the window when called
        win.destroy()

    #MAIN
    l1=Label(win,text=" player1 : X",font="times 18")
    l1.grid(row=0,column=1)
    l2=Label(win,text=" player2 : O",font="times 18")
    l2.grid(row=0,column=2)
     # combined building buttons and gridding the button
    b1=Button(win,width=20,height=10,command=lambda:click(1))
    b1.grid(row=1,column=1)
    b2=Button(win,width=20,height=10,command=lambda:click(2))
    b2.grid(row=1,column=2)
    b3=Button(win,width=20,height=10,command=lambda: click(3))
    b3.grid(row=1,column=3)
    b4=Button(win,width=20,height=10,command=lambda: click(4))
    b4.grid(row=2,column=1)
    b5=Button(win,width=20,height=10,command=lambda: click(5))
    b5.grid(row=2,column=2)
    b6=Button(win,width=20,height=10,command=lambda: click(6))
    b6.grid(row=2,column=3)
    b7=Button(win,width=20,height=10,command=lambda: click(7))
    b7.grid(row=3,column=1)
    b8=Button(win,width=20,height=10,command=lambda: click(8))
    b8.grid(row=3,column=2)
    b9=Button(win,width=20,height=10,command=lambda: click(9))
    b9.grid(row=3,column=3)
    lb=[b1,b2,b3,b4,b5,b6,b7,b8,b9] #Storing buttons in a list to reduce code size
    win.mainloop()
