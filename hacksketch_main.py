import sys
import serial
import pygame
from pygame.locals import *
import operator


X_DIM = 1024
Y_DIM = 1024

white = (255,255,255)
black = (0,0,0)

def column(matrix, i):
	return [row[i] for row in matrix]	

def fadeScreen():
	pygame.display.get_surface().fill((16,16,16), None, BLEND_RGBA_ADD)

def getColumn(multiList, col):
	return [x[col] for x in multiList]


pygame.init()
screen = pygame.display.set_mode((X_DIM, Y_DIM))
clock = pygame.time.Clock()
screen.fill(white)

arduino = serial.Serial('/dev/ttyACM0', 9600)

last10 = [[0]*3 for i in range(10)] # create 10 element queue for x,y,z accel values

lastDrawX = X_DIM/2
lastDrawY = Y_DIM/2

sinceErase = 0;

while 1:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit(0)

	clock.tick(60)
	pygame.display.update()

	tokens = arduino.readline().split()

	if(len(tokens)  == 5):
		last10.pop(0)
		last10.append([float(tokens[2]), float(tokens[3]), float(tokens[4])])

		drawX = int(tokens[0])
		drawY = int(tokens[1])

		# check for floating analog input and ignore unitl real input
		if((drawX>150 and drawX<950) and (lastDrawX<100 or lastDrawX>1000)):
			drawX = lastDrawX

		if((drawY>150 and drawY<950) and (lastDrawY<100 or lastDrawY>1000)):
			drawY = lastDrawY

		#print"x: %d\ny:%d\n" %(drawX, drawY)

		if(lastDrawX == X_DIM/2 and lastDrawY == Y_DIM/2):
			pygame.draw.circle(screen, black,(drawX, drawY), 0)
		elif((abs(lastDrawY-drawY) < 900) and (abs(lastDrawX-drawX) < 900)):
			pygame.draw.lines(screen, black, True, [(lastDrawX, lastDrawY), (drawX, drawY)], 2)

		lastDrawX = drawX
		lastDrawY = drawY

	sinceErase += 1


	#print "X: %f\nY: %f\nZ: %f\n" % (max(column(last10, 0)), max(column(last10, 1)), max(column(last10, 2)))
