#!/usr/bin/python
import os, sys, pygame, random
from pygame.locals import *
from stick_figure import *
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
pygame.display.set_caption("Kings Connected: start menu - dev")



class Menu(object):
	def __init__(self,size,screen):
		self.size = size
		self.screen = screen
		self.x = size[0] * 0.25
		self.width = size[0] * 0.5
		self.y = size[1] * 0.1
		self.height = size[1] * 0.2

		print self.size
		print self.x
		print self.width
		print self.y
		print self.height

	def draw_box(self,color):
		#pygame.draw.rect(screen,white,[x,y,50,75])

		pygame.draw.rect(screen,color,[self.x,self.y,self.width,self.height])

	def addText(self,text,color,font):
		font = pygame.font.SysFont('Arial', 12)
        # Rules status box. Need to add word wrap but it sorta works
		self.screen.blit(self.font.render(text, True, color), ((self.l+50), (self.t+25)))
	
	def start_game(self):
		draw_box(white)
		print "We're on the start menu!"

	def options(self):
		pass

	def exit(self,x,y):
		draw_box(self.screen,self.x,self.y,self.width,self.height)

main_menu = Menu(size,screen)


done = False
while done == False:
	# ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			print " Exiting program "
			done = True # Flag that we are done so we exit this loop

	main_menu.start_game

	screen.fill(black)


	main_menu.draw_box(white)
	#main_menu.draw_box(white,100,200)

	pygame.display.flip()
		# Limit to 20 frames per second
		# Limit changed between commits in dev versions to slow down debugging output. usually set between 2-10 FPS
	clock.tick(20)

pygame.quit()
