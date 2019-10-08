import sys, pygame
#from pygame import _view
from pygame.locals import *
from sys import exit

import time

import textBox
import box
import button

import math
#input_var = raw_input("Enter something: ")
#print "you entered " + str(input_var)

#DOTS for cursor:
#RELATIVITY GAME CODE
		
SPACE_BETWEEN_POINTS = 300
C = SPACE_BETWEEN_POINTS/2
#END RELATIVITY GAME CODE

	
def main(name):
	print str(name)
	print 'hello man'
	pygame.init()
	
	screen_width = 1300
	screen_height = 900
	
	clock = pygame.time.Clock()
	
	size = width, height = screen_width, screen_height
	screen = pygame.display.set_mode(size)
	
	#Variable declaration for cursor
	dot_image_file = 'Image/dot.png'
	dot = pygame.image.load(dot_image_file).convert()

	red_dot_image_file = 'Image/reddot.png'
	reddot = pygame.image.load(red_dot_image_file).convert()

	green_dot_image_file = 'Image/greendot.png'
	greendot = pygame.image.load(green_dot_image_file).convert()
	#End variable declaration for cursor.
	
	
	WHITE = (255, 255, 255)
	myfont = pygame.font.SysFont("comicsansms", 30)
	
	labelExample2 = myfont.render("Hello world", 1, (0,0,255))

	screen.blit(labelExample2, ((6*screen_width)/8, (4*screen_height)/5 + 10 + 1*40))
	
	mouseJustPressed = 0
	mouseHeld = 0
	mouseJustRelease = 0
	
	startServer = button.Button(200, 300, 250, 50, "testing", (0, 255 ,0), (255, 0 ,255))
	
	colourDatBox = 0
	
	onScreenText = ''
	
	textBox1 = textBox.TextBox(0,0,0,0, '', (255, 255, 255), (0, 0, 0))
	
	#Relativity game vars:
	#dx prev to erase prev:
	dxprev = 0

	dx=0.0
	px=0.0
	vx=0.0
	
	ax=1.0
	
	while 1==1:
		#Get mouse events:
		mouseJustPressed = 0
		mouseJustRelease = 0
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					mouseHeld=1
					mouseJustPressed = 1
			
			elif event.type == MOUSEBUTTONUP:
				if event.button == 1:
					mouseHeld = 0
					mouseJustRelease = 1
			
		#TODO: get th textbox that's focused on if possible, then update it!
		textBox1.dealWithKeyboard(event)
		mx,my = pygame.mouse.get_pos()
		
		
		textBox1.drawTextBox(screen, screen_width, screen_height)
		
		
		#print mouse cursor:
		if mouseJustPressed == 1 or mouseJustRelease==1:
			screen.blit(greendot, (mx-5, my-5), (0, 0, 10, 10))
		elif mouseHeld == 1:
			screen.blit(reddot, (mx-5, my-5), (0, 0, 10, 10))
		else:
			screen.blit(dot, (mx-5, my-5), (0, 0, 10, 10))
		
		
		#print str(mx) + ' ' + str(my)
		#screen_width = 1300
		#screen_height = 900
		
		#RELATIVITY GAME CODE
		
		
		#erase mesh from last frame
		for y in range(0, screen_height, SPACE_BETWEEN_POINTS):
			for x in range(0, screen_width, SPACE_BETWEEN_POINTS):
				pygame.draw.rect(screen, (0 ,0 ,0), (x-5 +(dxprev % SPACE_BETWEEN_POINTS), y-5, 10, 10))
		#end erase mesh from last frame
		
		for y in range(0, screen_height, SPACE_BETWEEN_POINTS):
			for x in range(0, screen_width, SPACE_BETWEEN_POINTS):
				screen.blit(greendot, (x-5 +(dx % SPACE_BETWEEN_POINTS), y-5), (0, 0, 10, 10))
		
		#If mouse held accelerate to the right else decelerate (and down go below 0)
		if mouseHeld == 1:
			px = px + 1.0
		else:
			px = px - 1.0
			if px < 0:
				px = 0
		
		lambdaNum = getLambda(vx)
		print("lambdaNum: " + str(lambdaNum))
		
		print("px: " + str(px))
		print("vx: " + str(vx))
		
		dxprev = dx
		
		#TODO: SOLVE p=v/(sqrt(1-(v^2-c^2)))
		#Maybe do a binary search?
		vx = 0.0
		for vtrial in range(0, C):
			if( vtrial * getLambda(vtrial) <= px):
				vx = vtrial
			else:
				break
		
		dx = dx + vx
		
		
		#END RELATITY GAME CODE
		
		labelExample = myfont.render("Mellow", 1, (0,255,0))
		goToServer = box.Box(100, 200, 250, 50)
		pygame.draw.rect(screen, (255, 0 ,255), goToServer.getCoordBox())
		screen.blit(dot, goToServer.getTopLeftBox(), goToServer.getCoordBox())
		screen.blit(labelExample, goToServer.getTopLeftBox())
		
		pressed = startServer.updateButtonAndCheckIfPressed(mx, my, mouseJustPressed, mouseJustRelease)
		startServer.printButton(pygame, screen)
		
		if pressed == 1:
			colourDatBox = colourDatBox + 1
		
		#Button reaction:
		if colourDatBox % 2 == 1:
			screen.blit(dot, (50, 50), (0, 0, 10, 10))
		else:
			pygame.draw.rect(screen, (0, 0 ,0), (50, 50, 10, 10))
		
		#Blinking:
		if shouldBlinkTextCursor() == 1:
			#TODO: make this a nice vertical line.
			screen.blit(dot, (100, 50), (0, 0, 10, 10))
		else:
			screen.blit(reddot, (100, 50), (0, 0, 10, 10))
		
		#pygame.draw.rect()
		
		pygame.display.update()
		clock.tick(60)
	
	print "bye"
	
PERIOD = 1000
SHOWCURSONTIME = 500
	
def shouldBlinkTextCursor():
	partOfCycle = round(time.time() * 1000) % PERIOD
	
	if partOfCycle < SHOWCURSONTIME:
		return 1
	else:
		return 0
		
		
def getLambda(v):
	return 1.0 /  math.sqrt(1.0 - ((1.0*v*v) / (1.0*SPACE_BETWEEN_POINTS*SPACE_BETWEEN_POINTS)))
	
if __name__ == "__main__":
	main('hello world')
