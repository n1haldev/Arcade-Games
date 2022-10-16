import turtle, random

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

turtlegame()
