#!/usr/bin/python
import os, sys
import pygame
import random
from pygame.locals import *
from stick_figure import *
from objects import *
import pygbutton

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
pygame.display.set_caption("Kings Connected - dev")


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Current position
x_coord=10
y_coord=10

x_speed=0
y_speed=0

facecards = {1: "A", 11: "J", 12: "Q", 13: "K"}

rules = {
	1: "Waterfall: everyone bottoms up, no one can stop drinking until the person to their right stops",
	2: "You: pick someone to drink",
	3: "Me: person who drew the card drinks",
	4: "Floor: Opposite of 7, everyone touches their hand to the floor, last one to do so drinks",
	5: "Guys: All guys drink",
	6: "Chicks: All girls drink",
	7: "Heaven: Opposite of 4, everyone reaches towards the sky/ceiling; last one up drinks",
	8: """Mate: Drawer of card chooses mate. Until another 8 is drawn, chosen person must drink whenever
	the person that chose them drinks""",
	9: "Rhyme: Drawer of card says a word, each subsequent player must say a word that rhymes with that word",
	10: "Categories: player chooses a category, each subsequent player says something relating to it",
	11: """Never have I ever: put up three fingers, take turns saying something you have never done. If anyone
	HAS done it they drop a finger and drink. First one with no fingers is out and drinks twice""",
	12: """Question: starting with the card being drawn, in order players take turns asking question.
	First person to answer with anything except a question drinks""",
	13: "Rule: Player that draws King gets to make a rule that will be in play until next king is drawn",
}
random_rule = random.randrange(1, 13)
# Set value for cards drawn
cards_drawn = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0}
total_cards = 0
def get_rule():
	random_rule = random.randrange(1, 13)
	if total_cards == 52:
		done = True
	elif cards_drawn[random_rule] <= 4:
		cards_drawn[random_rule] += 1
		total_cards += 1
		return random_rule
	else:
		get_rule()


#Pane_params = ((175, 450, 200, 100), 2)
Pane = Pane(screen,white,size,(size[0]/2-300),450,600,100)

buttonWhiteWinBg = pygbutton.PygButton((50, 50, 60, 30), 'White')
#Loop until the user clicks the close button.
done = False
pause = False

def draw_box(screen,x,y):
	pygame.draw.rect(screen,white,[x,y,50,50])
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
				pause = True
				print "System is paused"
			if event.key == pygame.K_RETURN:
				random_rule = random.randrange(1, 13)

				
			if 'click' in buttonWhiteWinBg.handleEvent(event):
				get_rule()
				print "button clicked"


		while pause == True:
			print "while loop: system paused until space pressed"
			for event in pygame.event.get():
				if event.type ==KEYUP:
					if event.key==K_SPACE:
						pause = False
						
	
	#random_rule = random.randrange(1, 12)
	print rules[random_rule]
	print cards_drawn

	#******************************************#
	# **** Keep all pre-move logic above! **** #
	#******************************************#

	# Set all movement changes below. All logic goes above
	
	
	x_coord = x_coord + x_speed
	y_coord = y_coord + y_speed
	# Start code to draw shit
	screen.fill(black)

	Pane.addRect()
	Pane.addText(rules[random_rule])

	# Draw the item
	draw_stick_figure(screen, white, x_coord, y_coord) 
	draw_box(screen, 1100, 100)

	#draw button
	buttonWhiteWinBg.draw(screen)


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