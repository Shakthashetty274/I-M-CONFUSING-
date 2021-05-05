# import the modules  
import tkinter 
import random 
  
# list of possible colour. 
colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown'] 
score = 0
  
# the game time left, initially 30 seconds. 
timeleft = 30
  
# function starts the game. 
def startGame(event): 
      
    if timeleft == 30: 
          
        # starting the countdown timer. 
        countdown() 
          
    # run the function to 
    # choose the next colour. 
    nextColour() 
  
# Function to choose and 
# display the next colour. 
def nextColour(): 
  
    # use the globally declared 'score' and also the timeleft
    # and 'play' variables above. 
    global score 
    global timeleft 
  
    # if a game is currently in play 
    if timeleft > 0: 
  
        # make the text entry box active. 
        e.focus_set() 
  
        # if the colour typed is equal 
        # to the colour of the text 
        if e.get().lower() == colours[1].lower(): 
              
            score += 1
  
        # clear the text entry box. 
        e.delete(0, tkinter.END) 
          
        random.shuffle(colours) 
          
        # change the colour to type, by changing the 
        # text _and_ the colour to a random colour value 
        label.config(fg = str(colours[1]), text = str(colours[0])) 
          
        # update the score. 
        scoreLabel.config(text = "Score: " + str(score)) 
  
  
# Countdown timer function  
def countdown(): 
  
    global timeleft 
  
    # if a game is in play 
    if timeleft > 0: 
  
        # decrement the timer. 
        timeleft -= 1
          
        # update the time left label 
        timeLabel.config(text = "Time left: "
                               + str(timeleft)) 
                                 
        # run the function again after 1 second. 
        timeLabel.after(1000, countdown) 
  
  
# Driver Code 
  
# create a GUI window 
root = tkinter.Tk() 
  
# set the title 
root.title("I'M CONFUSING") 
  
# set the size 
root.geometry("1980x1950") 

root.configure(bg='AntiqueWhite')
  
# add an instructions label 
instructions = tkinter.Label(root, text = "Type in the colour"
                        "of the words, and not the word text!", 
                                      font = ('Segoe Script', 25)) 
instructions.pack()  
  
# add a score label 
scoreLabel = tkinter.Label(root, text = "Press enter to start", 
                                      font = ('Verdana', 22)) 
scoreLabel.pack() 
  
# add a time left label 
timeLabel = tkinter.Label(root, text = "Time left : " +
              str(timeleft), font = ('Impact', 15)) 
                
timeLabel.pack() 
  
# add a label for displaying the colours 
label = tkinter.Label(root, font = ('Monotype Corsiva', 60)) 
label.pack() 
  
# add a text entry box for 
# typing in colours 
e = tkinter.Entry(root) 
  
# run the 'startGame' function  
# when the enter key is pressed 
root.bind('<Return>', startGame) 
e.pack() 
  
# set focus on the entry box 
e.focus_set() 
  
# run the GUI 
root.mainloop() 