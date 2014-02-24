#!/usr/bin/python
import pygame

# some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)

# Draw objects:

class Box(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def draw_box(self,screen,x,y):
		pygame.draw.rect(screen,white,[x,y,50,75])


	def bounding_box(self,screen,color,x,y,width,height):
		height = height * 0.5
		width = width * 0.5
		right = x + width
		left = x - width
		top = y - height
		bottom = y + height

		return {1: top, 2: right, 3: bottom, 4: left, 5: width, 6: height}

	def draw_bounding(self,screen,color,x,y,a,b):
		pygame.draw.rect(screen,color,[x,y,a,b])

	def mouse_tag(self,screen,color,x,y):
		#box = bounding_box(screen,color,x,y,50,50)
		draw_bounding(screen,color,x,y,50,50)

class Card(object):
	def __init__(self,x,y):
		self.x = x 
		self.y = y


class Pane(object):
    def __init__(self,screen,color,size,l,t,w,h):
        self.font = pygame.font.SysFont('Arial', 12)
        self.screen = screen
        self.color = color
        self.size = size
        self.l = l
        self.t = t
        self.w = w
        self.h = h
#        pygame.display.update()


    def addRect(self):
        #self.rect = pygame.draw.rect(self.screen, (self.color), (175, (self.size[1]-150), 200, 100), 2)
        self.rect = pygame.draw.rect(self.screen, (self.color), (self.l,self.t,self.w,self.h),2)
#        pygame.display.update()

    def addText(self,text):
        #self.screen.blit(self.font.render('This is the douchey status box I\'ll use for the rules at some point', True, (255,0,0)), (200, 100))
		self.screen.blit(self.font.render(text, True, (255,0,0)), ((self.l+50), (self.t+25)))

#        pygame.display.update()
