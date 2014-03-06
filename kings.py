#!/usr/bin/python
import os, sys, pygame, random, pygbutton
from pygame.locals import *
from stick_figure import *
#from objects import *
from class_layout import *
import platform

# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)


pygame.init()

# Game globals, screen size, game speed(clock) and the actual screen object, also title bar
# Set the width and height of the screen [width,height] (comes out to be Y, X. freaking wierd...)
size = [1200,600]
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Set screen parameters
# Outer limits
screen_bottom = size[1]
screen_right = size[0]

#set the actual size. set in var above for changability
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kings Connected - dev")

# End Pygame settings




# Current position of stick figure
x_coord=10
y_coord=10

x_speed=0
y_speed=0


#cardface = {1:"A",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K"}

rules = {
	1: "Waterfall: everyone bottoms up, no one can stop drinking until the person to their right stops",
	2: "You: pick someone to drink",
	3: "Me: person who drew the card drinks",
	4: "Floor: Opposite of 7, everyone touches their hand to the floor, last one to do so drinks",
	5: "Guys: All guys drink",
	6: "Chicks: All girls drink",
	7: "Heaven: Opposite of 4, everyone reaches towards the sky/ceiling; last one up drinks",
	8: """Mate: Drawer of card chooses mate. Until another 8 is drawn(or the rest of the game), chosen person must drink whenever
	the person that chose them drinks""",
	9: "Rhyme: Drawer of card says a word, each subsequent player must say a word that rhymes with that word",
	10: "Categories: player chooses a category, each subsequent player says something relating to it",
	11: """Never have I ever: put up three fingers, take turns saying something you have never done. If anyone
	HAS done it they drop a finger and drink. First one with no fingers is out and drinks twice""",
	12: """Question: starting with the card being drawn, in order players take turns asking question.
	First person to answer with anything except a question drinks""",
	13: "Rule: Player that draws King gets to make a rule that will be in play until next king is drawn",
}
random_rule = random.randrange(1, 14)
string_rule = str(random_rule)
print string_rule
# Set value for cards drawn
cards_drawn = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0}
total_cards = 0


#def get_rule():
#	rule = random.randrange(1, 14)
#	global total_cards
#	# For as long as the card drawn has already been drawn 4 times, re-draw
#	while cards_drawn[rule] >= 4:
#		rule = random.randrange(1,14)
#	
#	cards_drawn[rule] += 1
#	total_cards += 1
#	if total_cards >= 52:
#		return True
#	#done = True
#	else:
#		return rule
	

#Pane_params = ((175, 450, 200, 100), 2)
Pane = Pane(screen,white,size,(size[0]/2-300),450,600,100)

#Loop until the user clicks the close button.
done = False
pause = False


# Mouse stuff
mouse_pressed = False
mouse_down = False
mouse_released =False
target = None


Card = Card(screen,450,100,100,150,total_cards,cards_drawn)

# -------- Main Program Loop -----------
while done == False:
	# ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			print " Exiting program "
			done = True # Flag that we are done so we exit this loop


		# Get mouse position
		pos = pygame.mouse.get_pos()
		mouse_x = pos[0]
		mouse_y = pos[1]

		

		# ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
		# Mouse things
		mouse_col = collision_detect(mouse_x,mouse_y,1,1,1000,100,100,150,screen)

		if event.type == pygame.MOUSEBUTTONDOWN:
			if mouse_col is True:
				mouse_pressed = True
				mouse_down = True

		if event.type == pygame.MOUSEBUTTONUP:
			mouse_released = True
			mouse_down = False


		if mouse_pressed == True:
			mouse_col = collision_detect(mouse_x,mouse_y,1,1,Card.x,Card.y,Card.w,Card.h,screen)


			print "mouse was pressed!"
			print mouse_x, "mouse x position"
			print mouse_y, "mouse y position"
			#mouse_col = collision_detect(mouse_x,mouse_y,1,1,1000,100,100,150,screen)
			mouse_col = collision_detect(mouse_x,mouse_y,1,1,Card.x,Card.y,Card.w,Card.h,screen)

			print mouse_col,"\n"
			
		if mouse_released == True:
			#mouse_col = collision_detect(mouse_x,mouse_y,1,1,1000,100,100,150,screen)
			mouse_col = collision_detect(mouse_x,mouse_y,1,1,Card.x,Card.y,Card.w,Card.h,screen)



			if mouse_col is True:
				random_rule = Card.get_rule()
				string_rule = str(random_rule)
			if random_rule is True:
				done = True
			else:
				pass

			mouse_pressed = False
			mouse_released = False



		# Key press things
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
				random_rule = Card.get_rule()
				string_rule = str(random_rule)
				if random_rule is True:
					done = True
				else:
					pass



		while pause == True:
			print "while loop: system paused until space pressed"
			for event in pygame.event.get():
				if event.type ==KEYUP:
					if event.key==K_SPACE:
						pause = False
						
	
	#random_rule = random.randrange(1, 12)
	#print rules[random_rule]
	#print Card.cards_drawn
	#print Card.total_cards

	#******************************************#
	# **** Keep all pre-move logic above! **** #
	#******************************************#

	# Set all movement changes below. All logic goes above
	
	
	x_coord = x_coord + x_speed
	y_coord = y_coord + y_speed
	# Start code to draw shit
	screen.fill(black)

	if Card.total_cards > 0 and Card.total_cards < 51:
		Pane.addRect()
		Pane.addText(rules[random_rule])
	elif Card.total_cards >=51:
		Pane.addRect()
		Pane.addText("LAST")
		Pane.addText(rules[random_rule]+"Last")
	else:
		Pane.addRect()
		Pane.addText("\nPlease press enter or click on the card to draw a card")


	#if total_cards > 0 and total_cards < 51:
	#	Card.addText(rules[random_rule])
	#elif total_cards >=51:
	#	Pane.addText("LAST")
	#	Pane.addText(rules[random_rule]+"Last")
	#else:
	#	Pane.addText("\nPlease press enter or click on the card to draw a card")


	# Draw the item
	draw_stick_figure(screen, white, x_coord, y_coord) 
	
	Card.render(17)




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