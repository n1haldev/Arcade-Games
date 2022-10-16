from tkinter import *                                          #tkinter library for gui in Python
from tkinter.messagebox import showinfo,askyesno               
from tkinter.simpledialog import askstring
import mailing as em                                           #mailing.py is user-defined lib to handle mails during login and registration process from the user
from PIL import Image,ImageTk                                  #pillow to interact with images
import random,turtle                                           #random to generate coordinates of apple in the snake game 
import pygame                                                  #pygame to create interactive arcade games
from pygame.locals import *                                    
import time                                                    #time lib to control speed in the games present

def Gameon(back_buttonIMG):
    frame2.pack_forget()
    RorL.title("Tic-Tac-Toe Game")
    numbers=[1,2,3,4,5,6,7,8,9]
    # y='X' for player1 and 'O' for player2
    y=""
    # x is the counter to keep counting the number of chances
    x=0
    #boards is a list to store the mark with respect to the cell number
    boards=[""]*10
    counter1=0                      #counter1 stores points gained by user 1
    counter2=0                      #counter2 stores points gained by user 2

    def reset():                                        #reset funnction resets all ocuupied O-X field with Empty strings
        nonlocal boards,numbers,x,y,counter1,counter2
        x=0                         #x identifier used to decide which player's turn it is
        y=""                        #y identifier stores string X or O based on whose turn it is
        boards=[""]*10              #boards is a list of strings stored in grids of tic-tac-toe
        numbers=[1,2,3,4,5,6,7,8,9]     #list of ummbers to keep track of which grid the user has clicked
        counterlabel1.config(text=f'''Player 1 Score:{counter1}''')     #label to seamlessly display the score of user 1
        counterlabel2.config(text=f'''Player 2 Score:{counter2}''')     #label to seamlessly display the score of user 2
        for i in numbers:
            lb[i-1].config(text="")                     #configuring all existing grids to empty string due to reset
     
    def result(boards,mark):                #function to decide if there is a winer and who the winner is
        return ((boards[1] == boards[2] == boards [3] == mark) 
                or (boards[4] == boards[5] == boards [6] == mark) 
                or (boards[7] == boards[8] == boards [9] == mark)       #mark is X or O checked when user clicks on a grid
                or (boards[1] == boards[4] == boards [7] == mark) 
                or (boards[2] == boards[5] == boards [8] == mark)
                or (boards[3] == boards[6] == boards [9] == mark)
                or (boards[1] == boards[5] == boards [9] == mark) 
                or (boards[3] == boards[5] == boards [7] == mark))
                
    def decider(a,b,n):                             #function decider chnges the string to X or O based on user number and choice and grid
            nonlocal x,y,numbers,counter1,counter2
            x,y,num=a,b,n
            if x%2==0:              #deciding whose turn it is
                y='X'               #user 1 has X by default
                boards[num]=y       
            elif x%2!=0:            
                y='O'
                boards[num]=y
            lb[num-1].config(text=y,font="times 10") #Display X or O based on the button clicked by user
            x=x+1
            mark=y
            # Here we are calling the result() to decide whether we have got the winner or not
            if(result(boards,mark) and mark=='X' ):
                #If Player1 is the winner show a dialog box stating the winner
                showinfo("Result","Player 1 wins") 
                counter1+=1         #updating player1 score
                reset()             #resetting the board once we have player 1 as the winner
            elif(result(boards,mark) and mark=='O'):
                #If Player2 is the winner show a dialog box stating the winner
                showinfo("Result","Player 2 wins")      
                counter2+=1         #updating player2 score
                reset()             #resetting the board once we have player 2 as the winner
     
    def click(num):                 #function click handles all user input in the form of clicks on the grids of the tic-tac-toe
        nonlocal x,y,numbers
        """ To Check which button has been clicked to avoid over-writing"""
        if num in numbers:          #removes grid number already clicked avoiding double clicking of the same grid
            numbers.remove(num)     
            decider(x,y,num)        #checks if there is a winner
                 
        # If we have not got any winner, display match has been tied.
        if(x>8 and result(boards,'X')==False and result(boards,'O')==False):    #checking if it is a tie
            showinfo("Result","Match Tied")     #dialog box stating that the game is a draw
            reset()                    #resetting the board when we have no winner

    backbutton=Button(frame3,image=back_buttonIMG,command=lambda:f3_to_f2())    #backbutton is an image button that allows the user to exit tic-tac-toe game and back to the game selection screen 
    backbutton.grid(row=1,column=1)
    counterlabel1=Label(frame3,text="Player 1 Score:0")         #label showing player 1 score initially
    counterlabel1.grid(row=2,column=1)
    counterlabel2=Label(frame3,text="Player 2 Score:0")         #label showing player 2 score initially
    counterlabel2.grid(row=3,column=1)
    l1=Label(frame3,text=" player1 : X",font="times 18")        #label showing that player 1 has X
    l1.grid(row=0,column=1)
    l2=Label(frame3,text=" player2 : O",font="times 18")        #label showing that player 2 has O
    l2.grid(row=0,column=2)
     # combined building buttons and gridding the button
    b1=Button(frame3,width=24,height=12,command=lambda:click(1))        #buttons which call the click function when the user clicks a button in the grid
    b1.grid(row=1,column=6)                                             #passing the grid number as parameter
    b2=Button(frame3,width=24,height=12,command=lambda:click(2))
    b2.grid(row=1,column=7)
    b3=Button(frame3,width=24,height=12,command=lambda: click(3))
    b3.grid(row=1,column=8)
    b4=Button(frame3,width=24,height=12,command=lambda: click(4))
    b4.grid(row=2,column=6)
    b5=Button(frame3,width=24,height=12,command=lambda: click(5))
    b5.grid(row=2,column=7)
    b6=Button(frame3,width=24,height=12,command=lambda: click(6))
    b6.grid(row=2,column=8)
    b7=Button(frame3,width=24,height=12,command=lambda: click(7))
    b7.grid(row=3,column=6)
    b8=Button(frame3,width=24,height=12,command=lambda: click(8))
    b8.grid(row=3,column=7)
    b9=Button(frame3,width=24,height=12,command=lambda: click(9))
    b9.grid(row=3,column=8)
    lb=[b1,b2,b3,b4,b5,b6,b7,b8,b9] #Storing buttons in a list to simplify the code
    
    frame3.pack(expand=1)           
    
def registration(a,b,c,d):              #function to handle registration of new users
    f=open("UserDataBase.txt")          #a txt file to store user details in read mode
    content=(f.read().splitlines())     #splitting lines of user details to make sure that the account to be registered is new
    fw=open("UserDataBase.txt","a")     #opening txt file in append mode to make changes to details like password
    for m in content:
        x=m.split(",")
        if c!=d:                        #checking if user has entered the same password in usual and confirmed password text fields
            showinfo("Incorrect Input","Password and Confirm Password is different!")       #dialog box stating that inputs are different
            break
        if a==x[1]:                     #checking if given email already had an account with us 
            showinfo("Alert!","An account using the provided email already exists\n\tYou can try logging in!")  #dialog box stating that an account using the same password already exists
            break
        else:
            authentication=em.welcome(a,b)          #passing name and email-address of the user to send a Welcome email
            code=askstring("Mail confirmation","Please enter confirmation code that was mailed to you")     #asking the user to enter a code that was sent with the welcome email to make sure that the email is owned by the same user trying to register
            if code==authentication:                #checking if code sent an duser response is the same
                response=askyesno("Real Quick!","Would you like to enable 2FA and make your account more secure?")  #dialog box asking if they would like to approve additional login security measures
                if response=="Yes":                 #checking if they chose to enable 2FA
                    s="\n"+b+","+a+","+c+",2FA"     #storing user details in the user data base txt file
                    fw.write(s)
                    fw.close()                      #closing txt file
                    f2()                            #calling f2 function to change the frames
                    RorL.title("Game Selection")    #changing title of the window as the frame has changed
                    break
                else:
                    s="\n"+b+","+a+","+c            #same as above but when 2FA is not enabled by the user 
                    fw.write(s)
                    fw.close()
                    f2()
                    RorL.title("Game Selection")
                    break
                    
def Login(a,b):                 #function Login to handle logging in of existing users 
    f=open("UserDataBase.txt","r")      #opening txt file in read mode 
    content=(f.read()).splitlines()     #splitig line details to check login 
    c=1                 #a flag variable
    for m in content:   #checking list of user details
        x=m.split(",")
        if a==x[1]:     #checking if the entered mail exists in our data base 
            c=0
            if b==x[2]:     #checking if password entered by the user is correct
                if "2FA" in m:      #checking if user had opted for 2FA
                    authentication=em.two_FA(a,x[0])        #passing email-address and name of the user
                    code=askstring("2FA confirmation","Please enter the 6-digit 2FA code that was mailed to you") #confirming 2FA code sent to their email
                    if code==authentication:	
                        f2()		#if correct 2FA is entered frame 2 which contains the choices of many games is displayed 
                        RorL.title("Game Selection")
                        break
                else:
                    f2()		#if there was no 2FA enabled then frame 2, the choices of many games, is displayed
                    RorL.title("Game Selection")
                    break
            else:
                showinfo("Wrong password","The password you have entered is wrong")	
                break
    if c!=0:		#in case user tries to login through an email address that doesn't exist in out usedatabase.txt, we invite them to register a new account
        showinfo("Wrong email","The email you provided hasn't registered an account\n\tYou can try registering a new account!")

def fpass():	#to handle forgot password, we take email address and send them the password and request to delete the email after login for security
    a=askstring("Forgot Password","Please enter your email address")
    f=open("UserDataBase.txt","r")
    content=(f.read()).splitlines()
    for m in content:
        x=m.split(",")
        if a==x[1]:
            c=0
            em.send_pass(a,x[0],x[2])	#email will be sent with their password
            showinfo("Alert!","The password has been sent to your email,\nplease login and delete the email thereafter ")
    if c!=0:
        showinfo("Wrong Email","There is no Game account in the mail you specified!")	

def pong():	#pong game function
    pygame.mixer.init()
    pygame.mixer.music.load('Sadches - Retro arcade.mp3')	#plays a soothing background music while user plays pong
    pygame.mixer.music.play()
    
    # Functions
    def paddle_a_up():		#paddle a moves up
        global y
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

    def paddle_a_down():	#paddle a moves down
        global y
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

    def paddle_b_up():		#paddle b moves up
        global y
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():	#paddle b moves down
        global y
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)
    
    def resetpong():		#resets score and starts a new game
        global wn,score_a,score_b,x,y,paddle_a,paddle_b,tup,ball,pen
        wn = turtle.Screen()
        wn.title("Pong")	#game window characteristics
        wn.bgcolor("black")
        wn.setup(width=800, height=600)
        wn.tracer(0)
        # Score
        
        # Paddle A characteristics
        paddle_a = turtle.Turtle()
        paddle_a.speed(0)
        paddle_a.shape("square")
        paddle_a.color("white")
        paddle_a.shapesize(stretch_wid=5,stretch_len=1)
        paddle_a.penup()
        paddle_a.goto(-350, 0)

        # Paddle B characteristics
        paddle_b = turtle.Turtle()
        paddle_b.speed(0)
        paddle_b.shape("square")
        paddle_b.color("white")
        paddle_b.shapesize(stretch_wid=5,stretch_len=1)
        paddle_b.penup()
        paddle_b.goto(350, 0)

        # Ball characteristics
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 2
        ball.dy = 2
        
        #sleep timer, controls the speed of the ball.
        global x
        x=True
        
    def destroys():	#when back button is pressed, game window is exited and frame 2, with choice of many games, is displayed
        wn.bye()
        pygame.mixer.music.pause()	#background music stops as pong game has exited
        global x
        x=False
    tup=0.01		#tup a number to make the game progressively harder by increasing the ball speed
    score_a = 0		#Paddle A score
    score_b = 0		#Paddle B score
    #Pen characteristics
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal")) #resetting the scores of both the players 
    resetpong()
    # Keyboard bindings
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")
    wn.onkeypress(destroys,"space")
    x=True
    # Main game loop
    while x:
        wn.update()
        
        tup-=0.00001		#reducing sleep time to increase ball speed
        time.sleep(tup)
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking

        # Top and bottom
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Left and right
        if ball.xcor() > 350:
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) #updating score a when ball is hit by Paddle A
            ball.goto(0, 0)
            ball.dx *= -1

        elif ball.xcor() < -350:
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))	#updating score b when ball is hit by Paddle B
            ball.goto(0, 0)
            ball.dx *= -1

        # Paddle and ball collisions(reversing the direction of movement of the ball on hitting the paddle)
        if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1 	
        
        elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1

def turtlegame():
    l=[0,1,2,3,4]
    word_list=['which', 'their', 'wipro', 'there', 'could']
    word_q=['Used in questions to ask type of a subject','Used to refer ownership','A popular company Harsham Premji','Used to refer location','Used when hypothetically thinking']
    answernumber = random.choice(l)# choose a random word or question from the list
    answer=word_list[answernumber]
    answerq=word_q[answernumber]
    y = 250 # y location
    def draw_square(x,y,col): # takes in x,y coordinates and a color
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.fillcolor(col) # set the fillcolor
        turtle.begin_fill()     # start the filling color
        for i in range(4):     # drawing the square
            turtle.forward(50)
            turtle.right(90)
        turtle.end_fill() # ending the filling of the color

    def input_guess(prompt):
        my_input = turtle.textinput("5 letter word", prompt)
        if my_input == None: return "     " # if you press cancel or submit with nothing
        elif len(my_input) != 5: return my_input[0:5] #sends the first five characters
        else: return my_input.lower() #sends lower case of the word. Means case does not make a difference.

    def check_guess(my_input,answer,y):
        count = 0 #Need a count, because of for loop used
        x = -250 # x location
        for i in my_input:
            if i == answer[count]: draw_square(x,y,"green") #exact character match draws a green square
            elif i in answer: draw_square(x,y,"yellow") #else if character anywhere in word draws yellow
            else: draw_square(x,y,"red") # otherwise draws red
            count+=1 # add 1 to the count
            x += 75 # move x coordinate along by 75
        turtle.penup() #Moves the turtle penup
        turtle.goto(x,y-25) #Moves it slightly down for the word
        turtle.write(my_input,font=("Fixedsys", 15, "normal")) # font verdana, size 15, normal style

    for i in range(3): #Where the program starts
        guess_prompt = "What is guess "+str(i+1)+"?"+"\n"+answerq #Makes a nice string for the prompt
        my_input = input_guess(guess_prompt) #calls input_guess function
        check_guess(my_input,answer,y)  #checks the guess
        y -= 75 #y down by 75
        if my_input == answer:
            turtle.penup()
            turtle.goto(-300,-200) #Always draws the congratulations in the same place
            turtle.write("Well Done!",font=("Chiller", 60, "normal"))
            break
    else: #Only runs if the for loop executes completely. i.e. You've used all your guesses.
        turtle.penup()
        turtle.goto(-300,-200)
        turtle.write(answer,font=("Cooper Black", 42, "normal"))
    turtle.done() #Needs if you are using Pycharm and some other Python editors.

def rpsgame(back_buttonIMG):	#rock-paper-scissor game logic
    frame2.pack_forget()	
    RorL.title('Rock Paper Scissor!!')

    title=Label(frame4,text='\n Rock Paper Scissor!! \n',fg='grey')	#frame 4 containing rps game is mounted
    title.config(font=('Courier',40))
    title.grid(row=0,column=2,columnspan=5)

    backbutton=Button(frame4,image=back_buttonIMG,command=lambda:f4_to_f2())	#backbutton to exit the rps game
    backbutton.grid(row=1,column=1)
    
    computer_input=""	#computer vs you rps game
    playercounter=0	#user score
    computercounter=0	#computer score

    title2=Label(frame4,text='Enjoy the game......\n \n',fg='green')
    title2.config(font=('Courier',20))
    title2.grid(row=1,column=3)

    options=Label(frame4,text='Options:\n',fg='orange')
    options.config(font=('Courier',18))
    options.grid(row=3,column=1)

    opt=['rock','paper','scissor']	#choice
    def winner(player_input):		#decides winner if there is one and tie if both choose the same item
        nonlocal your_score,computer_score,computer_input,playercounter,computercounter
        computer_input=random.choice(opt)
        
        if player_input==computer_input:	# Tie condition
            title2.config(text="It is a Tie!")
            computer_choice.config(text="Computer's choice-->"+computer_input)
            your_choice.config(text="Your choice-->"+player_input)
        elif (player_input=="rock" and computer_input=="paper") or (player_input=="scissor" and computer_input=="rock") or (player_input=="paper" and computer_input=="scissor"):			# Computer victory condition
            title2.config(text="Computer won!")
            computercounter+=1
            computer_choice.config(text="Computer's choice-->"+computer_input)
            your_choice.config(text="Your choice-->"+player_input)
            computer_score.config(text="Computer's Score-->"+str(computercounter))
        else:					# User victory condition
            title2.config(text="You win!")
            playercounter+=1
            your_score.config(text="Your Score-->"+str(playercounter))
            computer_choice.config(text="Computer's choice-->"+computer_input)
            your_choice.config(text="Player choice-->"+str(player_input))

    #buttons
    rock=Button(frame4,text='ROCK',width=15,command=lambda:winner("rock"))
    rock.grid(column=2,row=4)

    paper=Button(frame4,text='PAPER',width=15,command=lambda:winner("paper"))
    paper.grid(row=4,column=3)

    scissor=Button(frame4,text='SCISSOR',width=15,command=lambda:winner("scissor"))
    scissor.grid(row=4,column=4)

    your_choice=Label(frame4,text='Your choice-->(playername)')
    your_choice.grid(row=6, column=1)

    #results
    your_score=Label(frame4,text=f'''Your Score-->{playercounter}''')
    your_score.grid(row=6,column=3)

    computer_choice=Label(frame4,text=f'''Computer's choice-->{computer_input}''')
    computer_choice.grid(row=7,column=1)

    computer_score=Label(frame4,text=f'''Computer's Score-->{computercounter}''')
    computer_score.grid(row=7,column=3)
    frame4.pack()

def showpass(checkb,entry):	# shows password entered is checkbox is checked else by defualt shows password characters as '*'s
    if checkb.var.get():
        entry.config(show="")
    else:
        entry.config(show="*")

def SnakeGames():		# Snake and apple game using pygame
    SIZE=40
    pause=True

    class Apple:		
        def __init__(self,parent_screen):	# first position of apple
            self.parent_screen=parent_screen
            self.image=pygame.image.load("apple.jpg").convert()
            self.x=120
            self.y=120

        def draw(self):		# drawing apple on x and y co-ordinates
            self.parent_screen.blit(self.image,(self.x,self.y))
            pygame.display.flip()

        def move(self):		# move the apple elsewhere when apple is consumed
            self.x=random.randint(1,12)*SIZE
            self.y=random.randint(1,8)*SIZE
            

    class Snake:		
        def __init__(self,parent_screen,length): # starting point of the snake
            self.length=length
            self.parent_screen=parent_screen
            self.block=pygame.image.load("block.jpg").convert()
            self.x=[SIZE]*length
            self.y=[SIZE]*length
            self.direction="down"

        def inc_length(self):	# increasing the lenght of the snake on consuming the apple
            self.length+=1
            self.x.append(-1)
            self.y.append(-1)

        def draw(self):		# drawing the snake on the screen
            self.parent_screen.fill((110,110,5))
            for i in range(self.length):
                self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
            pygame.display.flip()

        def move_left(self):		# changing the direction of the snake to the left direction
            self.direction="left"

        def move_right(self):		# changing the direction of the snake to the right direction
            self.direction="right"

        def move_up(self):		# changing the direction of the snake to up direction
            self.direction="up"

        def move_down(self):		# changing the directiom of the snake to down direction
            self.direction="down"

        def walk(self):			# moving the snake in the set direction

            for i in range(self.length-1,0,-1):
                self.x[i]=self.x[i-1]
                self.y[i]=self.y[i-1]
            if self.direction=="up":
                self.y[0]-=40
            if self.direction=="down":
                self.y[0]+=40
            if self.direction=="right":
                self.x[0]+=40
            if self.direction=="left":
                self.x[0]-=40
            self.draw()


    class Game:
        def __init__(self):	# setting up the game window
            pygame.init()
            self.surface=pygame.display.set_mode((750,500))
            self.surface.fill((110,110,5))
            self.snake=Snake(self.surface,1)
            self.snake.draw()
            self.apple=Apple(self.surface)
            self.apple.draw()
        #snake colliding with apple
        def is_collision(self,x1,y1,x2,y2):	# handling the snake and apple collision
            if x1>=x2 and x1<x2+SIZE:
                if y1>=y2 and y1<y2+SIZE:
                    pygame.mixer.init()
                    pygame.mixer.music.load('ding.mp3')
                    pygame.mixer.music.play()
                    return True

        def display_score(self):		# displaying the score
            font=pygame.font.SysFont('arial',30)
            score=font.render(f"Score: {self.snake.length-1}",True,(255,255,255))
            self.surface.blit(score,(500,10))

        def play(self):				# game starts and snake stars moving
            self.snake.walk()
            self.apple.draw()
            self.display_score()
            pygame.display.flip()
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y): # if snake collides with apple
                self.apple.move()
                self.snake.inc_length()

            for i in range(3,self.snake.length):	
                if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):	# if snake collides with itself game ends
                    pygame.mixer.init()
                    pygame.mixer.music.load('crash.mp3')
                    pygame.mixer.music.play()
                    raise "Game Over"

        def show_game_over(self):     	# handles end of game and resets the score
            self.surface.fill((110,110,5))
            font=pygame.font.SysFont('arial',30)
            line1=font.render(f"Game is Over, Your Score: {self.snake.length-1}",True,(255,255,255))
            self.surface.blit(line1,(100,200))
            line2=font.render("To play again press Enter. To exit press Escape",True,(255,255,255))
            self.surface.blit(line2,(100,250))
            pygame.display.flip()
            
            
            
        def run(self):		# runs infinite loop waiting for user keypresses
                running=True
                pause=False

                while running:
                    for event in pygame.event.get():
                        if event.type==KEYDOWN:
                            if event.key==K_ESCAPE:
                                running=False

                            if event.key==K_RETURN:
                                pause=False
                                self.snake.length=1
                            if event.key==K_ESCAPE:
                                pause=True
                                
                                self.show_game_over()
                            if event.key== K_UP:
                                self.snake.move_up()
                            if event.key== K_DOWN:
                                self.snake.move_down()
                            if event.key== K_LEFT:
                                self.snake.move_left()
                            if event.key== K_RIGHT:
                                self.snake.move_right()
                        
                        elif event.type==QUIT:
                            running=False
                            
                    try:
                        if not pause:
                            self.play()
                    except Exception as e:
                        self.show_game_over()
                        pause=True
                    time.sleep(0.25)
    if __name__=="__main__":
        game=Game()
        game.run()
        

RorL=Tk()                                               
RorL.title("Welcome to the Arcade Games")              
RorL.geometry("1500x1000")

frame5=Frame(RorL)      # frame 5 has the pong game

frame4=Frame(RorL)	# frame 4 has the Rock-Paper-Scissor game

frame3=Frame(RorL)	# frame 3 has the Tic-Tac-Toe game

frame2=Frame(RorL)						   # frame 2 has the choice of games													
bgIMG=ImageTk.PhotoImage(Image.open("GSelectionIMG.jpg"))          #setting background image of window present during login and game selection
bglabel=Label(frame2,image=bgIMG)
bglabel.pack()
logoutIMG=ImageTk.PhotoImage(Image.open("LogoutIMG1.jpg"))         #image of the logout button
logoutbutton=Button(frame2,image=logoutIMG,bg="black",command=lambda:f2_to_f1())        
SelectLabel=Label(frame2,text="Choose a Game To Play:",font="times 20",bg="black",fg="Red")
btttIMG=ImageTk.PhotoImage(Image.open("TTTimage.png"))              #an image button to select Tic-Tac-Toe game
back_buttonIMG=ImageTk.PhotoImage(Image.open("back_buttonIMG.jpg"))         #back button image button to exit a selected game so the user can choose to play another game at any point of time
bTTT=Button(frame2,image=btttIMG,width=200,height=200,command=lambda:Gameon(back_buttonIMG))       #function Gameon takes us to the Tic-Tac-Toe game
bTTT.place(x=50,y=120)
SelectLabel.place(x=550,y=50)
logoutbutton.place(x=1200,y=20)
rpsIMG=ImageTk.PhotoImage(Image.open("rpsIMG.png"))             #an image button to select the rock paper-scissor-game
rpsgamebutton=Button(frame2,image=rpsIMG,width=200,height=200,command=lambda:rpsgame(back_buttonIMG))   #function rpsgame takes us to the rock-paper-scissor game
rpsgamebutton.place(x=300,y=120)
turtlegameIMG=ImageTk.PhotoImage(Image.open("turtle_gameIMG.jpg"))      #an image button to select the turtle based Wordle game
turtlegamebutton=Button(frame2,image=turtlegameIMG,width=200,height=200,command=lambda:turtlegame())       #function turtlegame takes us to the turtle based wordle game
turtlegamebutton.place(x=550,y=120)
PongIMG=ImageTk.PhotoImage(Image.open("pong_IMG.jpg"))      #an image button to select the Pong game
Ponggamebutton=Button(frame2,image=PongIMG,width=200,height=200,command=lambda:pong())  #function pong takes us to the turtle based Pong game
Ponggamebutton.place(x=800,y=120)
snakegameIMG=ImageTk.PhotoImage(Image.open("snakegame.png"))       #an image button to select the Snake and apple game
SnakeGameButton=Button(frame2,image=snakegameIMG,width=200,height=200,command=lambda:SnakeGames())      #function SnakeGames takes user to the Snake and Apple game
SnakeGameButton.place(x=50,y=350)

frame1=Frame(RorL)          #frame1 contains the widgets for the login and registration page
bgimg=ImageTk.PhotoImage(Image.open("RorLBGI.jpg"))     #login page background
bglabel=Label(frame1,image=bgimg)       
bglabel.pack()
rml=Label(frame1,text="Enter your email address:")     #rml-registration mail label
rnl=Label(frame1,text="Enter your name:")               #rnl-registration name label
rpl=Label(frame1,text="Enter your Password")           #rpl-registration password label
rcpl=Label(frame1,text="Confirm your Password")         #rcpl-registration confirmed password label
rpe=Entry(frame1,width=40,show="*")                     #rpe-registration password entry, masked as * by default
rcpe=Entry(frame1,width=40,show="*")                    #rcpe-registration confirmed password label, masked as * by default
rme=Entry(frame1,width=40)                              #rme-registration mail entry
rne=Entry(frame1,width=40)                              #registration name entry
rml.place(x=400,y=200)                                  
rme.place(x=400,y=225)
rnl.place(x=400,y=250)
rne.place(x=400,y=275)
rpl.place(x=400,y=300)
rpe.place(x=400,y=325)
rcpl.place(x=400,y=380)
rcpe.place(x=400,y=405)
lml=Label(frame1,text="Enter your email address:")      #login mail label
lml.place(x=750,y=200)                                  
lme=Entry(frame1,width=40)                              #login mail entry
lme.place(x=750,y=225)
lpl=Label(frame1,text="Enter your Password")            #login password label
lpl.place(x=750,y=250)
lpe=Entry(frame1,width=40,show="*")                     #login password entry
lpe.place(x=750,y=275)
Registerbg=ImageTk.PhotoImage(Image.open("RegisterIMG.jpg"))       #register image button to create new account
Loginbg=ImageTk.PhotoImage(Image.open("LoginIMG.jpg"))              #login image button to enter existing account
rb=Label(frame1,image=Registerbg,bg="black")                        
lb=Label(frame1,image=Loginbg,bg="black")                                      
register=Button(frame1,text="Register",width=10,height=2,bg="green",command=lambda:registration(rme.get(),rne.get(),rpe.get(),rcpe.get()) if rme.get()!="" and rne.get()!="" and rpe.get()!="" and rcpe.get()!="" else showinfo("Warning!","Please fill all fields!")) #mail#name#pass#confirmpass
login=Button(frame1,text="Login",width=10,height=2,bg="green",command=lambda:Login(lme.get(),lpe.get()) if lme.get()!="" and lpe.get()!="" else showinfo("Warning!","Please fill all fields!"))		# login button
forgotpass=Button(frame1,text="Forgot Password",width=12,height=1,bg="yellow",command=lambda:fpass())	# forgot password button
forgotpass.place(x=900,y=300)
register.place(x=400,y=460)
login.place(x=750,y=330)
rb.place(x=400,y=100)
lb.place(x=750,y=100)

cbrpe,cbrcpe,cb=0,0,0	# checkbox button(show password) for registraion password entry and login password entry
cbrpe=Checkbutton(frame1,text="Show Password",onvalue=True,offvalue=False,command=lambda:showpass(cbrpe,rpe))
cbrpe.var=BooleanVar(value=False)
cbrpe['variable']=cbrpe.var
cbrpe.place(x=400,y=350)
cbrcpe=Checkbutton(frame1,text="Show Password",onvalue=True,offvalue=False,command=lambda:showpass(cbrcpe,rcpe))
cbrcpe.var=BooleanVar(value=False)
cbrcpe['variable']=cbrcpe.var
cbrcpe.place(x=400,y=430)
cb=Checkbutton(frame1,text="Show Password",onvalue=True,offvalue=False,command=lambda:showpass(cb,lpe))
cb.var=BooleanVar(value=False)
cb['variable']=cb.var
cb.place(x=750,y=300)

def f4_to_f2():		# changes the frame rendered from Rock-Paper-Scissor game to Game selection frame
    frame4.pack_forget()
    RorL.title("Game Selection")
    f2()
    
def f3_to_f2():		# changes the frame rendered from Tic-Tac-Toe game to the Game selection frame
    frame3.pack_forget()
    RorL.title("Game Selection")
    f2()
    
def f2_to_f1():		# changes the frame from the Game selection frame to the login/registration page
    frame2.pack_forget()
    f1()

def f1():		# renders frame 1 which is the login/registration page
    frame1.pack()

def f2():		# renders frame 2 which is the Game selection frame
    rme.delete(0,END)
    rne.delete(0,END)
    rpe.delete(0,END)
    rcpe.delete(0,END)
    
    lme.delete(0,END)
    lpe.delete(0,END)
    frame1.pack_forget()
    frame2.pack()
    
f1() # renders frame 1 which is the login page at the start of the executing this program

RorL.mainloop()

