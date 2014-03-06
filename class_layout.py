#!/usr/bin/python
import random
from objects import *



# Trying to create a good class layout. Define all objects, essentially. list goes as follows:
# - Card
# - List of previously drawn cards
# - Rules: seperate class so that rules can be changed in the options
# - Game mode: continueous draw until quit; 52 card limit; 4 kings limit; custom; <= this class for contains the game end modules based of chosen moded
# - Players: a class to control all players, maybe a new class for turns



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
	15: "Please draw a card"
}
cardface = {0:0,1:"A",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K"}



class Card(object):
	def __init__(self,screen,x,y,w,h,total_cards,cards_drawn):
		self.screen = screen
		self.font = pygame.font.SysFont('Arial', 17)
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.total_cards = total_cards
		self.cards_drawn = cards_drawn
		self.rule = 0

	def draw_box(self,screen):
		pygame.draw.rect(screen,white,[self.x,self.y,self.w,self.h])

	# Get attributes of rule
	def get_rule(self):
		self.rule = random.randrange(1, 14)
		# For as long as the card drawn has already been drawn 4 times, re-draw
		while self.cards_drawn[self.rule] >= 4:
			self.rule = random.randrange(1,14)
	
		self.cards_drawn[self.rule] += 1
		self.total_cards += 1
		if self.total_cards >= 52:
			return True
		#done = True
		else:
			return self.rule


	# All logic designed to change the location of the card
	def move_card(self,mouse_pos):
		pass


	# All classes should have a render to make a "render all objects" class possible
	# This class, if passed a list of Card[] should suffice to make card rendering easy enough
	def render(self,font_size):
		# Draw card box
		self.draw_box(self.screen)
		# Top left
		add_text((self.x+7),(self.y+5),cardface[self.rule],font_size,red,self.screen)
		# Top Right
		add_text((self.x+80),(self.y+5),cardface[self.rule],font_size,red,self.screen)
		# Bottom left
		add_text((self.x+7),(self.y+127),cardface[self.rule],font_size,red,self.screen)
		# Bottom right
		add_text((self.x+80),(self.y+127),cardface[self.rule],font_size,red,self.screen)
		# Center
		add_text((self.x+35),(self.y+60),cardface[self.rule],font_size,red,self.screen)


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
	


class End(object):
	def __init__(self,card):
		self.card = card

