#!/usr/bin/python
import pygame

# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)


def draw_stick_figure(screen,color,x,y):
	# Head
	pygame.draw.ellipse(screen,color,[1+x,y,10,10],0)
	# Legs
	pygame.draw.line(screen,color,[5+x,17+y],[10+x,27+y],2)
	pygame.draw.line(screen,color,[5+x,17+y],[x,27+y],2)
	# Body
	pygame.draw.line(screen,color,[5+x,17+y],[5+x,7+y],2)
	# Arms
	pygame.draw.line(screen,color,[5+x,7+y],[9+x,17+y],2)
	pygame.draw.line(screen,color,[5+x,7+y],[1+x,17+y],2)

def draw_ball(screen,x,y):
	# Head
	pygame.draw.ellipse(screen,white,[1+x,y,20,20],10)

def draw_lives(screen,x,y):
	pygame.draw.rect(screen,white,[x,y,50,50])

def draw_blocker(screen,color,x,y,height,width):
	pygame.draw.rect(screen,color,[x,y,height,width])

def draw_bullet(screen,x,y):
	pygame.draw.line(screen,red,[10+x,y],[x,y],2)
	

