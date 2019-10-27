import sys, pygame
#from pygame import _view
from pygame.locals import *
from sys import exit

import time

import textBox
import box
import button

import coord

import math
#input_var = raw_input("Enter something: ")
#print "you entered " + str(input_var)

#DOTS for cursor:
#RELATIVITY GAME CODE
		
SPACE_BETWEEN_POINTS = 300
C = SPACE_BETWEEN_POINTS/5
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
	
	#For red dots:
	vanglered = 0.0
	
	while 1==1:
		#Get mouse events:
		mouseJustPressed = 0
		mouseJustRelease = 0
		
		pygame.draw.rect(screen, (0 ,0 ,0), (0, 0, screen_width, screen_height))
		
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
		
		relativistic_space_between_points_x=int((1.0*SPACE_BETWEEN_POINTS)/(getLambda(vx)))
		
		print("relativistic_space_between_points_x: " + str(relativistic_space_between_points_x))
		
		stretch_factor=int((5.0)/(getLambda(vx)))
		
		for y in range(my%SPACE_BETWEEN_POINTS, screen_height, SPACE_BETWEEN_POINTS):
			for x in range(mx%relativistic_space_between_points_x, screen_width, relativistic_space_between_points_x):
				#screen.blit(greendot, (x-5 +(dx % relativistic_space_between_points_x), y-5), (0, 0, 10, 10))
				#Just stretch space:
				screen.blit(greendot, (x-stretch_factor , y-5), (0, 0, max(2*stretch_factor, 1), 10))
				
		
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
		
		vxfraction = 0.0
		for vtrial2 in range(0, 1000):
			vspeedTrial=1.0*vx + (1.0*vtrial2)/1000.0
			if( vspeedTrial * getLambda(vspeedTrial) <= px):
				vxfraction =  vtrial2/1000.0
			else:
				break
		
		vx = 1.0*vx + 1.0*vxfraction
		dx = dx + (1.0*vx)/100.0
		
		
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
		
		#Print coord stuff:
		#for xpoint in range(int(math.floor(-screen_width* getLambda(vx))), int(math.ceil(screen_width* getLambda(vx))), SPACE_BETWEEN_POINTS):
		#	for ypoint in range(int(math.floor(-screen_height* getLambda(vx))), int(math.ceil(screen_height* getLambda(vx))), SPACE_BETWEEN_POINTS):
		
		#for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				vanglered += math.pi / 180.0
			if event.key == pygame.K_d:
				vanglered -= math.pi / 180.0
		
		if vanglered > 2 * math.pi:
			vanglered -= 2 * math.pi
		elif vanglered < -2 * math.pi:
			vanglered += 2 * math.pi
			
		print "angle: " + str(int(vanglered * 180.0 / math.pi))
		
		#for xpoint in range(0, int(math.ceil(screen_width * getLambda(vx))), SPACE_BETWEEN_POINTS):
		#	for ypoint in range(0, int( math.ceil(screen_height* getLambda(vx))), SPACE_BETWEEN_POINTS):
		
		shipx = 200
		shipy = 200
		
		screen.blit(greendot, (shipx-5 , shipy-5), (0, 0, 10, 10))
		screen.blit(greendot, (shipx-5 + int(10 * math.cos(vanglered)) , shipy-5 +  int(10 * math.sin(vanglered)) ), (0, 0, 10, 10))
		
		pointInSpace = coord.Coord(300, 200)
		newCoord = getContractedCoord(coord.Coord(shipx,shipy), pointInSpace, coord.Coord(vx*math.cos(vanglered),vx*math.sin(vanglered)))
		
		#if newCoord.x < screen_width - 5 and newCoord.y < screen_height -5 and newCoord.x - 5 > 0 and newCoord.y - 5 > 0:
		#	screen.blit(reddot, (newCoord.x-5 , newCoord.y-5), (0, 0, 10, 10))
		
		for xpoint in range(0, int(math.ceil(screen_width)), SPACE_BETWEEN_POINTS):
			for ypoint in range(0, int( math.ceil(screen_height)), SPACE_BETWEEN_POINTS):
				pointInSpace = coord.Coord(xpoint, ypoint)
				newCoord = getContractedCoord(coord.Coord(shipx,shipy), pointInSpace, coord.Coord(vx*math.cos(vanglered),vx*math.sin(vanglered)))
				
				if newCoord.x < screen_width - 5 and newCoord.y < screen_height -5 and newCoord.x - 5 > 0 and newCoord.y - 5 > 0:
					screen.blit(reddot, (newCoord.x-5 , newCoord.y-5), (0, 0, 10, 10))
				
				
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


def getContractedCoord(pointO, point, vel):
	#Edge case when velocity is 0 or the two points are at the same spot:
	if getLength(vel) == 0.0 or (point.x == pointO.x and point.y == pointO.y):
		return coord.Coord(point.x, point.y)
	
	vector2 = getDiff(point, pointO)
	
	#todo: WHAT'S GOING ON?
	#TODO: try to reduce copy/paste code?
	vectora1 = getLength(vector2) * getCosTheta(vel, vector2) * vel.x / ( getLength(vel) * getLambdaVector(vel) )
	vectora2 = getLength(vector2) * getCosTheta(vel, vector2) * vel.y / ( getLength(vel) * getLambdaVector(vel) )
	
	vectorb1 = getLength(vector2) * getSinTheta(vel, vector2) * getCounterClockPerp(vel).x /(getLength(vel))
	vectorb2 = getLength(vector2) * getSinTheta(vel, vector2) * getCounterClockPerp(vel).y /(getLength(vel))

	finalCoordx = pointO.x + vectora1 + vectorb1
	finalCoordy = pointO.y + vectora2 + vectorb2
	
	#print("New coord vector A: " + str(vectora1) + " , " + str(vectora2))
	#print("New coord vector B: " + str(vectorb1) + " , " + str(vectorb2))
	
	return coord.Coord(finalCoordx, finalCoordy)

def getSum(pointa, prointb):
	return coord.Coord(pointa.x + pointb.x, pointa.y + pointb.y)

#input1 - input2
def getDiff(pointb, pointa):
	return coord.Coord(pointb.x - pointa.x, pointb.y - pointa.y)
		
		
def getTheta(coord1, coord2):
	return signTheta(coord1, coord2) * getAbsTheta(coord1, coord2)

#This seems like it's not needed... I'm confused though
#Coord 1 is reference dir
def dirTheta(coord1, coord2):
	if(coord1.x * coord2.y - coord1.y*coord2.x > 0.0):
		return 1.0
	else:
		return -1.0
		
def getAbsTheta(coord1, coord2):
	math.acos(Math.abs(getCosTheta(coord1, coord2)))
		
def getSinTheta(coord1, coord2):
	return (1.0 *coord1.x * coord2.y - 1.0 * coord1.y*coord2.x )/(getLength(coord1) * getLength(coord2))
		
def getCosTheta(coord1, coord2):
	return (1.0 * getScalarMult(coord1, coord2)) / (1.0 * getLength(coord1) * getLength(coord2))
		
def getScalarMult(coord1, coord2):
	return 1.0 * coord1.x*coord2.x + 1.0 * coord1.y*coord2.y

def getLength(vector):
	return 1.0*math.sqrt(vector.x*vector.x + vector.y*vector.y)

def getCounterClockPerp(vector):
	return coord.Coord(0.0 - vector.y, 1.0 * vector.x)

def getLambdaVector(vector):
	if( getLength(vector) >= C):
		print "ERROR: vector is going faster than C!"
		sys.exit()
	
	return getLambda(getLength(vector))

def getLambda(v):
	return 1.0 /  (1.0*math.sqrt(1.0 - ((1.0*v*v) / (1.0*C*C))))
	
if __name__ == "__main__":
	main('hello world')
