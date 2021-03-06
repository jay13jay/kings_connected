#!/usr/bin/python
import pygame

# some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)


# Collision detection:

def collision_detect(x1,y1,w1,h1,x2,y2,w2,h2,screen):
	
	if x2+w2>=x1>=x2 and y2+h2>=y1>=y2:
		return True
	elif x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2:
		return True
	elif x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2:
		return True
	elif x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2:
		return True
	else:
		return False

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

	def get_rule():
		rule = random.randrange(1, 14)
		global total_cards
		# For as long as the card drawn has already been drawn 4 times, re-draw
		while cards_drawn[rule] >= 4:
			rule = random.randrange(1,14)
	
		cards_drawn[rule] += 1
		total_cards += 1
		if total_cards >= 52:
			return True
		#done = True
		else:
			return rule

	def render(self,total_cards):
		if total_cards > 0 and total_cards < 51:
			Pane.addRect()
			Pane.addText(rules[random_rule])
		elif total_cards >=51:
			Pane.addRect()
			Pane.addText("LAST")
			Pane.addText(rules[random_rule])
		else:
			Pane.addRect()
			Pane.addText("\nPlease press enter or click on the card to draw a card")


def add_text(x,y,text,size,color,screen):
	font = pygame.font.SysFont('Arial', size)
	screen.blit(font.render(text, True, (color)), (x,y))




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
        # Rules status box. Need to add word wrap but it sorta works
		self.screen.blit(self.font.render(text, True, (255,0,0)), ((self.l+50), (self.t+25)))

#        pygame.display.update()
