import sys
import serial
import pygame
from pygame.locals import *
import operator

# dimensions of screen based on interval arduino gives for simplicity
X_DIM = 1024
Y_DIM = 1024

white = (255,255,255)

# ugly, I know. just wanted to add some pretty colours
colourList = [(0,0,0),
(0,0,0),
(0,0,0),
(0,0,0),
(0,0,0),
(0,0,0),
(0,0,0),
(105,105,105),
(128,128,128),
(169,169,169),
(192,192,192),
(211,211,211),
(220,220,220),
(128,0,0),
(139,0,0),
(165,42,42),
(178,34,34),
(220,20,60),
(255,0,0),
(255,99,71),
(255,127,80),
(205,92,92),
(240,128,128),
(233,150,122),
(250,128,114),
(255,160,122),
(255,69,0),
(255,140,0),
(255,165,0),
(255,215,0),
(184,134,11),
(218,165,32),
(238,232,170),
(189,183,107),
(240,230,140),
(128,128,0),
(255,255,0),
(154,205,50),
(85,107,47),
(107,142,35),
(124,252,0),
(127,255,0),
(173,255,47),
(0,100,0),
(0,128,0),
(34,139,34),
(0,255,0),
(50,205,50),
(144,238,144),
(152,251,152),
(143,188,143),
(0,250,154),
(0,255,127),
(46,139,87),
(102,205,170),
(60,179,113),
(32,178,170),
(47,79,79),
(0,128,128),
(0,139,139),
(0,255,255),
(0,255,255),
(224,255,255),
(0,206,209),
(64,224,208),
(72,209,204),
(175,238,238),
(127,255,212),
(176,224,230),
(95,158,160),
(70,130,180),
(100,149,237),
(0,191,255),
(30,144,255),
(173,216,230),
(135,206,235),
(135,206,250),
(25,25,112),
(0,0,128),
(0,0,139),
(0,0,205),
(0,0,255),
(65,105,225),
(138,43,226),
(75,0,130),
(72,61,139),
(106,90,205),
(123,104,238),
(147,112,219),
(139,0,139),
(148,0,211),
(153,50,204),
(186,85,211),
(128,0,128),
(216,191,216),
(221,160,221),
(238,130,238),
(255,0,255),
(218,112,214),
(199,21,133),
(219,112,147),
(255,20,147),
(255,105,180),
(255,182,193),
(255,192,203),
(250,235,215),
(245,245,220),
(255,228,196),
(255,235,205),
(245,222,179),
(255,248,220),
(255,250,205),
(250,250,210),
(255,255,224),
(139,69,19),
(160,82,45),
(210,105,30),
(205,133,63),
(244,164,96),
(222,184,135),
(210,180,140),
(188,143,143),
(255,228,181),
(255,222,173),
(255,218,185),
(255,228,225),
(255,240,245),
(250,240,230),
(253,245,230),
(255,239,213),
(255,245,238),
(245,255,250),
(112,128,144),
(119,136,153),
(176,196,222),
(230,230,250)]

# based on excel plot in this repo, tested x, y, and z maximas. Find the highest if in this window of values and taadaa!
def checkShake(shakeList, sinceShake):
	# dont wanna do this too quick to avoid double counts of the same peak
	shake = False
	returnVal = sinceShake

	xMax = max(map(abs, getColumn(shakeList, 0)))
	yMax = max(map(abs, getColumn(shakeList, 1)))
	zMax = max(map(abs, getColumn(shakeList, 2)))

	# print out max vals
	#print "X: %f\nY: %f\nZ: %f\n" % (xMax, yMax, zMax)

	# based on the values in excel plot, works pretty good 8)
	if(sinceShake>4 and (xMax>3 or yMax>2.5 or zMax>2.5)):
		fadeScreen()
		returnVal = 0

	# give back the index of the counter
	return returnVal	

# the magic that slowly 
def fadeScreen():
	pygame.display.get_surface().fill((21,21,21), None, BLEND_RGBA_ADD)

# given a multidimensional array, return the ith column
def getColumn(multiList, col):
	return [x[col] for x in multiList]

# pygame init stuff
pygame.init()
screen = pygame.display.set_mode((X_DIM, Y_DIM))
clock = pygame.time.Clock()
screen.fill(white)

# read from the arduino
arduino = serial.Serial('/dev/ttyACM0', 9600)

# sliding window, used so that values aren't double counted
last10 = [[0]*3 for i in range(10)] # create 10 element queue for x,y,z accel values (sliding window)

# "last" x and y dimensions
lastDrawX = X_DIM/2
lastDrawY = Y_DIM/2

sinceErase = 0;

while 1:
	# check if we quit
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit(0)

	sinceErase = checkShake(last10, sinceErase)

	# pygame stuff
	clock.tick(60)
	pygame.display.update()

	# tokens from the arduino, see arduino file for index meanings
	tokens = arduino.readline().split()

	# sometimes arduino gives us garbage, this helps a bit
	if(len(tokens) == 6):
		# retrieve accel values and maintain sliding window
		last10.pop(0)
		last10.append([float(tokens[2]), float(tokens[3]), float(tokens[4])])

		# retrieve inputs from arduino
		drawX = int(tokens[0])
		drawY = int(tokens[1])

		# last minute addition, just works. dont worry about this
		colour = int(tokens[5]) / (1096 / (len(colourList)))
		colourTup = colourList[colour]

		# check for floating analog input and ignore unitl real input
		if((drawX>100 and drawX<950) and (lastDrawX<50 or lastDrawX>975)):
			drawX = lastDrawX

		if((drawY>100 and drawY<950) and (lastDrawY<50 or lastDrawY>975)):
			drawY = lastDrawY

		# if you wanna print out some coordinates
		#print"x: %d\ny:%d\n" %(drawX, drawY)

		# draw lines unless we in the centre (just starting out)
		if(lastDrawX == X_DIM/2 and lastDrawY == Y_DIM/2):
			pygame.draw.circle(screen, colourTup,(drawX, drawY), 0)
		elif((abs(lastDrawY-drawY) < 900) and (abs(lastDrawX-drawX) < 900)):
			pygame.draw.lines(screen, colourTup, True, [(lastDrawX, lastDrawY), (drawX, drawY)], 2)

		# not a bad idea to keep track of these later
		lastDrawX = drawX
		lastDrawY = drawY

	sinceErase += 1