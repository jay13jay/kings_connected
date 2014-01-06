#!/usr/bin/python
import os, sys
import pygame
import random
from pygame.locals import *


# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)


pygame.init()


# Set the width and height of the screen [width,height] (comes out to be Y, X. freaking wierd...)
size = [1200,600]


# Set screen parameters
# Outer limits
screen_bottom = size[1]
screen_right = size[0]

#set the actual size. set in var above for changability
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tower defense game - dev")


# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Current position
x_coord=10
y_coord=10
x_speed=0
y_speed=0

facecards = {1: "A", 10: "J", 11: "Q", 12: "K"}

rules = {
	1: "Waterfall",
	2: "You",
	3: "Me",
	4: "Floor:\n Everyone touches their hand to the floor, last one to do so drinks",
	5: "Guys: \n All guys drink",
	6: "Chicks: \n All girls drink",
	7: "Heaven: \n Opposite of 4, everyone reaches towards the sky/ceiling; last one up drinks",
	8: "Mate: \n Drawer of card chooses mate. Until another 8 is drawn, chosen person must drink whenever the person that chose them drinks",
	9: "Rhyme: \n Drawer of card says a word, each subsequent player must say a word that rhymes with that word",
	10: """Never have I ever:
	Each player puts up 3 fingers, then take turns in order saying something they have never done
	first person with all fingers down must drink""",
	11: """Question: starting with the card being drawn, in order players take turns asking question. First person to answer with
	anything except a question drinks""",
	12: "Rule: Player that draws King gets to make a rule that will be in play until next king is drawn",
}


#Loop until the user clicks the close button.
done = False
pause = False
# -------- Main Program Loop -----------
while done == False:
	# ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			print " Exiting program "
			done = True # Flag that we are done so we exit this loop
			

		# ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
		if event.type == pygame.KEYDOWN:
			# Figure out if it was an arrow key. If so
			# adjust speed.
			if event.key == pygame.K_LEFT:
				x_speed = -7
			if event.key == pygame.K_RIGHT:
				x_speed = 7
			if event.key == pygame.K_UP:
				y_speed = -7
			if event.key == pygame.K_DOWN:
				y_speed = 7
			#if event.key == pygame.K_SPACE:
				#pause = False
				

		if event.type == pygame.KEYUP:
			# If it is an arrow key, reset vector back to zero
			if event.key == pygame.K_LEFT:
				x_speed = 0
			if event.key == pygame.K_RIGHT:
				x_speed = 0
			if event.key == pygame.K_UP:
				y_speed = 0
			if event.key == pygame.K_DOWN:
				y_speed = 0	
			if event.key == pygame.K_SPACE:
				pause = False
				print "System is paused"
		while pause == False:
			print "while loop: system paused until space pressed"
			for event in pygame.event.get():
				if event.type ==KEYUP:
					if event.key==K_SPACE:
						pause = True
				
	
	random_rule = random.randrange(1, 12)
	print random_rule
	print rules[random_rule]

	#******************************************#
	# **** Keep all pre-move logic above! **** #
	#******************************************#

	# Set all movement changes below. All logic goes above




	
	
	x_coord = x_coord + x_speed
	y_coord = y_coord + y_speed
	# Start code to draw shit
	screen.fill(black)


	# Draw the item
	#draw_stick_figure(screen, x_coord, y_coord) 


	# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

	# Update the screen with what we've drawn.
	pygame.display.flip()
		# Limit to 20 frames per second
		# Limit changed between commits in dev versions to slow down debugging output. usually set between 2-10 FPS
	clock.tick(20)
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()