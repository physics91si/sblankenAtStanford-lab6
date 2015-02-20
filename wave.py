#! /usr/env/bin

"""This file produces the solution of the 1-D wave equation with fixed boundary conditions. It is your job to fill in the simulate() and update() functions."""


#The following statements are used to set up the live plotting and to import numpy and matplotlib.
import matplotlib
matplotlib.use("TKAgg")
import numpy as np
import matplotlib.pyplot as plt
plt.ion()
plt.hold(0)


def init():
	"""This function initialises the x-values, as well as the functional form of the y values, 2 time steps before the start of the simulation. It is currently set to produce a stationary gaussian. If you implement the simulation correctly, it will split into two gaussians travelling in opposite directions."""
	dx = 0.05 # the spatial stepping for the x values
	dt = 0.05 # the time step of the simulation
	c = 1 # the wave velocity in the simulation
	x = np.arange(-5,5,dx) # produce an initial set of x-values
	y = np.exp(-x**2)# produce an initial set of y-values
	y_next = np.exp(-x**2) # produce the next timestep of y-values (in a second order pde we need two conditions to fully specify the problem.
	simulate(y,y_next,c,dt,dx) #call the actual simulation




def simulate(y_old, y_curr, c, dt, dx):
	t_end = 100
	t = 0
	y_new = np.zeros(len(y_old)) #initialize the array of y-values
	while t < t_end:
		update(y_old,y_curr,y_new,dx,dt,c) #call update and have it write the next value set of y-values into the y_new array, given the old and current values of the y array.
		y_old = 1.0*y_curr #update the old and current y-values
		y_curr = 1.0*y_new

		#YOUR CODE: insert a call to plot the current y values here#

		#END YOUR CODE#

		#These lines customize the plot and force it to update.
		plt.ylim([-1,1])
		plt.gcf().canvas.flush_events()
		plt.show()
		t += dt
		print t #You can delete this line. It is just there to give you the current time step.



def update(y_old, y_curr, y_new, dx, dt, c):
"""This function should loop over all elements (except for the first and the last) in y_new and set the i'th element according to the rule
y_new[i] = (dt*c/dx)**2 * (y_curr[i+1] + y_curr[i-1] - 2*y_curr[i]) + 2*y_curr[i] - y_old[i]

Additionally, the first and last elements of y_new should be set to zero, to comply with the boundary conditions. The function currently does nothing."""
	pass

		
		
init()	#call init() to start the program
