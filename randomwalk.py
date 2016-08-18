#The following code describes a simple 1D random walk
#where the walker can move either forwards or backwards.  There is an
#equal probability to move either forwards or backwards with each step.



#Numeric Python library
import numpy as np


#Random number library
import random


#Plotting libary
from matplotlib import pyplot as plt


#Number of steps.  Chosen as 50 in this case.
N_steps = 100


#probability of a step going in either direction.
#Set to 0.5, meaning that walker is equally likely to move
#forwards or backwards with each step.
prob = 0.5



#Define the random walk function.  N in this case is the number of steps and
#p is the probablity threshold of going either forwards or backwards.  'line' is a string
#that will describe the marker and line style for a plot of the random walk.
def SimpleRandomWalk(N, p, line):


    #Create an array of positions for the walker.  And initialize the first position
    #to be the origin (zero).  The array will be the same size as the number of steps.
    #A position counter variable is also used, which is initialized to zero as well.
    position = np.empty(N)
    position[0] = 0
    pos_counter = 0

    #Array containing the full range of the number of possible steps taken.
    steps = np.arange(N)


    #Start the random walk.
    for i in range(1,N):


        #Generate a random probability value between 0 and 1.
        test = random.random()


        #Chechk the value of the probability generated.  If it is > or equal to 0.5, increment the step forwards.
        #If it is less than 0.5, increment a step backwards instead.  Keep track of the position counter after
        #updating it.
        if test >= p:
            pos_counter += 1
        else:
            pos_counter -= 1

        #Fill the current position array index with the current value of the position counter from the loop.
        position[i] = pos_counter



    #Generate a plot of walker position vs. the number of steps taken.  Line is a string that will describe the
    #markers and line type used to plot the random walk.
    plt.plot(steps, position, line)
    plt.xlabel('Steps taken')
    plt.ylabel('Distance from Starting Position')


    return None


#Create a new figure to plot the random walk.
plt.figure()

#Function call to generate and plot the first random walk with circular markers and a dotted line.
SimpleRandomWalk(N_steps, prob, line = 'o--')


#Hold the first random walk on the plot.
plt.hold(True)


#Function call to generate and plot a second random walk using a full line.
SimpleRandomWalk(N_steps, prob, line = '-')


#Show both random walks on the plot.
plt.show()