# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:30:02 2018

@author: ml17kfma
"""

"""
in this mode we creat agents that have a location which is craeted randomly between 0 and 299, these agents are moving randomly and eating 
the given environment from a file called ( in2.txt). Also agents share thier store with other agents within a neighbourhood if it in a certain distance

"""
#import libraries, time and agentframework
import random
import operator
import matplotlib.pyplot
import agentframework
import matplotlib.animation 
import tkinter
matplotlib.use('TkAgg')
import time


# start time runing of the model
start = time.clock ()               

# determain the number of agents in the model:
num_of_agents = 10#3#10#2#10
#num_of_iterations = 100#3 # this replaced by the update function
agents = []
# determin the distance of sharing the food between agents
neighbourhood = 40
# this describe the chance of moving each agents which is here 40%
probabilityMove = 0.4
# this give all agents a specific location each time the model run  
variety = 40
# create printing method to print values frequently:
printlevel1 = 1
printlevel2 = 2

# create a window as a user interface to run the model
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



# load environment 
print("Step 1: Load environment")
data = open("M:\Python Scripts\in2.txt")
#data = open("M:\Python Scripts\in.txt")
environment = []
for line in data: 
    parsed_line = str.split(line,",")
    rowlist = [] 
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)

data.close()
    

# Make the agents.
print("Step 2: Create agents")
for i in range(num_of_agents):
     agents.append(agentframework.Agent(i, environment, i * variety, probabilityMove, printlevel2))


carry_on = True

# Move and eat and share    
def update(frame_number):
    
    global carry_on
    fig.clear()
    
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    
    print("Step 3: Move, eat and share")
    #agentframework.print1("Move, eat")
    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share(neighbourhood,agents,i)
        
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

    
    if random.random() < 0.01:
        carry_on = False
        print("stopping condition")

#

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 200) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()
   
    
    
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()



end = time.clock()
print ("time = " + str(end - start))


# displey the agents after the stop of the model
print("Step 4: Resulting agents")
for i in range(num_of_agents):
     print(agents[i])
     
