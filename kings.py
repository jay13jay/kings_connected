#!/usr/bin/python
import os, sys, pygame, random
from pygame.locals import *
from stick_figure import *
#from objects import *
from class_layout import *
import platform

# Define strings for RGB colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)


###############
# Game globals#
###############

#Call the pygame engine
pygame.init()
# Set the width and height of the screen [width,height]
size = [1200,600]

# Game system clock
clock = pygame.time.Clock()


# Screen edges
screen_bottom = size[1]
screen_right = size[0]

# Instantiate the screen object and set its caption
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kings Connected - dev")

# Set the number of players
player_list = ["player1","player2","player3","player4"]

# Stick figure starting position and velocity
x_coord=10
y_coord=10

x_speed=0
y_speed=0


#cardface = {1:"A",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K"}

# Dict of numbers(cards) matching their corresponding rules
rules = {
	0: "START",
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


# random rule is for accessing the dict defined above
random_rule = 0
# Dictionary counter for each card drawn
cards_drawn = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0}

# Counter for the total cards drawn
total_cards = 0

# Card sizes
card_size = [100,150]

# Instantiate Pane object, a rect with method for applying text
Pane = Pane(screen,white,size,(size[0]/2-300),450,600,100)


# Done ends game on True
done = False
# Stops the while loop until a keypress on True
pause = False

###############
# Mouse stuff #
###############

# Old mouse coordinates for semi-stateful mouse movement tracking
old_mouse_pos = [0,0]
# Was mouse just pressed? Is only True on loop that mouse was pressed
mouse_pressed = False
# Stays true until mouse is released
mouse_down = False
# Was mouse just released? Is True only on loop that mouse was released
mouse_released =False
# For tracking object under mouse pointer
target = None


# NEED TO READDRESS AT A LATER DATE


#card_list = []
#start_pos = [250,100]
#for i in player_list:
	# Doing this part wrong. will address later
#	i = Card(screen,start_pos,card_size,total_cards,cards_drawn)
#	card_list.append(i)
#	print card_list
#	start_pos[0]
#print start_pos
#print card_size


Card1 = Card(screen,450,100,100,150,total_cards,cards_drawn)
Card2 = Card(screen,600,100,100,150,total_cards,cards_drawn)
Card3 = Card(screen,450,300,100,150,total_cards,cards_drawn)
Card4 = Card(screen,600,300,100,150,total_cards,cards_drawn)


card_objects = [Card1,Card2,Card3,Card4]


# -------- Main Program Loop -----------
while done == False:
	# ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			print " Exiting program "
			done = True # Flag that we are done so we exit this loop


		# Get mouse position
		mouse_pos = pygame.mouse.get_pos()
		mouse_x = mouse_pos[0]
		mouse_y = mouse_pos[1]

		# Mouse things
		for i in card_objects:
			mouse_col_i = collision_detect(mouse_x,mouse_y,1,1,i.x,i.y,i.w,i.h,screen)
			#print "collision with",i,"is:\t",mouse_col_i

			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				old_mouse_pos = mouse_pos

				mouse_pressed = True
				mouse_down = True

			if mouse_pressed is True and mouse_col_i is True and target is None:
				target = i
			
			

			if event.type == pygame.MOUSEBUTTONUP:
				mouse_released = True
				mouse_down = False
				mouse_pos = pygame.mouse.get_pos()
				pos_change_x = old_mouse_pos[0] - mouse_pos[0]
				pos_change_y = old_mouse_pos[1] - mouse_pos[1]
				# Release target
			
		
			# While mouse buttonis down, if object is under target, move it
			if mouse_down == True:
				mouse_pos = pygame.mouse.get_pos()
				pos_change_x = old_mouse_pos[0] - mouse_pos[0]
				pos_change_y = old_mouse_pos[1] - mouse_pos[1]
				old_mouse_pos = mouse_pos
				if target != None:
					target.x = target.x - pos_change_x
					target.y = target.y - pos_change_y
				
			#if mouse_pressed == True:
			#	mouse_col = collision_detect(mouse_x,mouse_y,1,1,Card1.x,Card1.y,Card1.w,Card1.h,screen)
				#old_mouse_pos = mouse_pos
			
			# when mouse is released, draw card, check for game end
			if mouse_released == True:
				target = None

				if mouse_col_i is True:
					random_rule = i.get_rule()
					string_rule = str(random_rule)
					total_cards = total_cards+1
				#if random_rule is True:
				#	done = True
				if total_cards >= 52:
					print "Game over!"
					done = True
				else:
					pass

			# Reset the pressed and released variables, as they should only action once 
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
				random_rule = Card1.get_rule()
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

	#if Card1.total_cards > 0 and Card1.total_cards < 51:
	#	Pane.addRect()
	#	Pane.addText(rules[random_rule])
	#elif Card1.total_cards >=51:
	#	Pane.addRect()
	#	Pane.addText("LAST")
	#	Pane.addText(rules[random_rule]+"Last")
	#else:
	#	Pane.addRect()
	#	Pane.addText("\nPlease press enter or click on the card to draw a card")

	if total_cards > 0 and total_cards < 51:
		Pane.addRect()
		Pane.addText(rules[random_rule])
	elif total_cards >=51:
		Pane.addRect()
		Pane.addText("LAST")
		Pane.addText(rules[random_rule]+"Last")
	else:
		Pane.addRect()
		Pane.addText("\nPlease press enter or click on the card to draw a card")
	

	# Draw the item
	draw_stick_figure(screen, white, x_coord, y_coord) 
	
	# This is the old way, trying to make sure that multiple objects can be just added rather than having to go back over and have to
	# instantiate it, move it, render it etc. Trying to put shit in lists and read off those, but I'm probably going to have to read
	# up on a proper way to do this so I can stop wasting my time.
	#Card1.render(17)
	#Card2.render(20)
	for card in card_objects:
		# Render card, pass it the font size
		card.render(15)




	# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

	# Update the screen with what we've drawn.
	pygame.display.flip()
		# Limit to 20 frames per second
		# Limit changed between commits in dev versions to slow down debugging output. usually set between 2-10 FPS
	clock.tick(1120)
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

