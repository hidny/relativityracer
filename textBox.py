#from pygame import _view
from pygame.locals import *

import pygame
import box

class TextBox:
	
	box = box.Box(0,0,0,0)
	colour = (0, 0, 0)
	
	labelColour = 0
	
	isFocussed = 0
	isPressedDown = 0
	
	currentText = ''
	isKeyHeldDown = 0
	isDeletingText = 0
	
	
	def __init__(self, x, y, width, height, currentText, labelColour, bkColour):
		self.box = box.Box(x, y, width, height)
		
		self.currentText = currentText
		self.labelColour = labelColour
		self.colour = bkColour
	
	def getTopLeftBox(self):
		return self.box.getTopLeftBox(self.x, self.y)
	
	def getCoordBox(self):
		return self.box.getCoordBox()
	
	def isWithinBox(self, x, y):
		return self.box.isWithinBox(x, y)
	
	#TODO: have a variable for the currently selected textbox.
	def updateButtonAndCheckIfPressed(self, x, y, mouseJustPressed, mouseJustRelease):
		if self.isWithinBox(x, y) == 0:
			self.isFocussed = 0
			self.isPressedDown = 0
		else:
			self.isFocussed = 1
			if mouseJustPressed == 1:
				self.isPressedDown = 1
		
		if mouseJustRelease == 1 and self.isFocussed == 1 and self.isPressedDown == 1 and self.isWithinBox(x, y) == 1:
			self.isPressedDown = 0
			return 1
		else:
			if  mouseJustRelease == 1:
				self.isPressedDown = 0
			return 0
	
	
	#TODO: autoprint and auto delete when button is held.
	def dealWithKeyboard(self, event):
		#events = pygame.event.get()
		#for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				location -= 1
			if event.key == pygame.K_RIGHT:
				location += 1
			if event.key == pygame.K_a:
				self.currentText = self.currentText + 'a'
			if event.key == pygame.K_b:
				self.currentText = self.currentText + 'b'
			if event.key == pygame.K_c:
				self.currentText = self.currentText + 'c'
			if event.key == pygame.K_d:
				self.currentText = self.currentText + 'd'
			if event.key == pygame.K_e:
				self.currentText = self.currentText + 'e'
			
			if event.key == pygame.K_f:
				self.currentText = self.currentText + 'f'
			if event.key == pygame.K_g:
				self.currentText = self.currentText + 'g'
			if event.key == pygame.K_h:
				self.currentText = self.currentText + 'h'
			if event.key == pygame.K_i:
				self.currentText = self.currentText + 'i'
			if event.key == pygame.K_j:
				self.currentText = self.currentText + 'j'
			
			if event.key == pygame.K_k:
				self.currentText = self.currentText + 'k'
			if event.key == pygame.K_l:
				self.currentText = self.currentText + 'l'
			if event.key == pygame.K_m:
				self.currentText = self.currentText + 'm'
			if event.key == pygame.K_n:
				self.currentText = self.currentText + 'n'
			if event.key == pygame.K_o:
				self.currentText = self.currentText + 'o'
			
			if event.key == pygame.K_p:
				self.currentText = self.currentText + 'p'
			if event.key == pygame.K_q:
				self.currentText = self.currentText + 'q'
			if event.key == pygame.K_r:
				self.currentText = self.currentText + 'r'
			if event.key == pygame.K_s:
				self.currentText = self.currentText + 's'
			if event.key == pygame.K_t:
				self.currentText = self.currentText + 't'
			
			if event.key == pygame.K_u:
				self.currentText = self.currentText + 'u'
			if event.key == pygame.K_v:
				self.currentText = self.currentText + 'v'
			if event.key == pygame.K_w:
				self.currentText = self.currentText + 'w'
			if event.key == pygame.K_x:
				self.currentText = self.currentText + 'x'
			if event.key == pygame.K_y:
				self.currentText = self.currentText + 'y'
			if event.key == pygame.K_z:
				self.currentText = self.currentText + 'z' 
			if event.key == pygame.K_z:
				self.currentText = self.currentText + 'z'
			
			if event.key == pygame.K_SPACE:
				self.currentText = self.currentText + ' '
			if event.key == pygame.K_ASTERISK:
				self.currentText = self.currentText + '*'
			if event.key == pygame.K_PLUS:
				self.currentText = self.currentText + '+'
			if event.key == pygame.K_COMMA:
				self.currentText = self.currentText + ','
			if event.key == pygame.K_PERIOD:
				self.currentText = self.currentText + '.'
			if event.key == pygame.K_MINUS:
				self.currentText = self.currentText + '!'
			if event.key == pygame.K_EXCLAIM:
				self.currentText = self.currentText + '!'
			if event.key == pygame.K_QUESTION:
				self.currentText = self.currentText + '?'
				
			if event.key == pygame.K_HASH:
				self.currentText = self.currentText + '#'
		
			if event.key == pygame.K_BACKSPACE:
				#if len(currentText) >= 1:
				print 'What'
				self.currentText = self.currentText[0:-1]
				self.isDeletingText = 1
			self.isKeyHeldDown = 1
			print 'keydown'
		else:
			if event.type == pygame.KEYUP:
				print 'keyup'
				self.isKeyHeldDown = 0
				self.isDeletingText = 0
			elif self.isKeyHeldDown == 1 and len(self.currentText) > 0 and self.isDeletingText == 0:
				self.currentText = self.currentText + self.currentText[-1]
			elif self.isKeyHeldDown == 1 and len(self.currentText) > 0 and self.isDeletingText == 1:
				self.currentText = self.currentText[0:-1]
				
	def getCurrentText(self):
		return self.currentText
		
	#TODO: get rid of screen_width and screen height params.
	def drawTextBox(self, screen, screen_width, screen_height):
		#TODO: make this customizable.
		myfont = pygame.font.SysFont("comicsansms", 30)
	
		labelExample3 = myfont.render(str(self.currentText), 1, (0,0,255))
		#pygame.draw.rect()
		#draw a rectangle shape
		pygame.draw.rect(screen, (0,0,0), ((1*screen_width)/32, (4*screen_height)/5 + 10 + 3*40, 1000, 100 ))
		
		screen.blit(labelExample3, ((1*screen_width)/32, (4*screen_height)/5 + 10 + 3*40))
	