#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Boyd Gibson
#
# Created:     03/11/2022
# Copyright:   (c) Boyd Gibson 2022
#-------------------------------------------------------------------------------
#class imports
from maze import Maze
from rat import Rat

#add in the pygame imports
import random, sys, copy, os, pygame
from pygame.locals import *

maze = Maze()
rat = Rat("^", 4, 1)

FPS = 30                    # frames per second to update the screen
WINWIDTH = 800              # width of the program's window, in pixels
WINHEIGHT = 600             # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2) #you need to know 1/2 sizes so you can
HALF_WINHEIGHT = int(WINHEIGHT / 2) #place things centrally

# The total width and height of each tile in pixels.
TILEWIDTH = 64
TILEHEIGHT = 64
TILEFLOORHEIGHT = 64

BRIGHTBLUE = (  0, 170, 255)
WHITE      = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

#A dictionary of the images used.  You can then use#floor, wall etc
#in place of the whole pathname

IMAGESDICT = {'floor': pygame.image.load("Cookies/Tile.jpg"),
              'wall': pygame.image.load("Cookies/Tile.jpg"),
              'cake': pygame.image.load("Cookies/Cake.jpg"),
              'monster': pygame.image.load("Cookies/Cookie.jpg"),
              'spacer': pygame.image.load("Cookies/Tile.jpg") }

TILEMAPPING = { '#':IMAGESDICT['wall'],
                ' ':IMAGESDICT['floor'],
                '@':IMAGESDICT['cake'],
                '/':IMAGESDICT['spacer'],
                '^':IMAGESDICT['monster']}

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('Cookie Monster v 1.00')
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)




def moveRatRight():
    #moving the rat to the right....
    #BEFORE you move the rat, check he CAN move!
    x = maze.getCharAtPos(rat.getRow(), rat.getCol() + 1)
    if x == "#":
        #print "This is a wall!"
        pass
    else:
        #if it is not a wall, maybe it is a tasty sprout?
        if x == "@":
            #print "Yum yum! Dinner time!"
            rat.eatSprouts()
            maze.eatSprouts()
        maze.clearAtPos(rat.getRow(), rat.getCol())
        rat.moveRight()
        maze.placeRat(rat.getChar(), rat.getRow(), rat.getCol())
    print (maze.toString())
    print (rat.toString())


def moveRatLeft():
    #moving the rat to the right....
    #BEFORE you move the rat, check he CAN move!
    x = maze.getCharAtPos(rat.getRow(), rat.getCol() - 1)
    if x == "#":
        #print "This is a wall!"
        pass
    else:
        #if it is not a wall, maybe it is a tasty sprout?
        if x == "@":
            #print "Yum yum! Dinner time!"
            rat.eatSprouts()
            maze.eatSprouts()
        maze.clearAtPos(rat.getRow(), rat.getCol())
        rat.moveLeft()
        maze.placeRat(rat.getChar(), rat.getRow(), rat.getCol())
    print (maze.toString())
    print (rat.toString())

#define functions for moveRatUp() moveRatDown() moveRatLeft()

def moveRatUp():
    #moving the rat to the right....
    #BEFORE you move the rat, check he CAN move!
    x = maze.getCharAtPos(rat.getRow()-1, rat.getCol())
    if x == "#":
        print ("This is a wall!")
    else:
        #if it is not a wall, maybe it is a tasty sprout?
        if x == "@":
            print ("Yum yum! Dinner time!")
            rat.eatSprouts()
            maze.eatSprouts()
        maze.clearAtPos(rat.getRow(), rat.getCol())
        rat.moveUp()
        maze.placeRat(rat.getChar(), rat.getRow(), rat.getCol())
    print (maze.toString())
    print (rat.toString())

def moveRatDown():
    #moving the rat to the right....
    #BEFORE you move the rat, check he CAN move!
    x = maze.getCharAtPos(rat.getRow()+1, rat.getCol())
    if x == "#":
        print ("This is a wall!")
    else:
        #if it is not a wall, maybe it is a tasty sprout?
        if x == "@":
            print ("Yum yum! Dinner time!")
            rat.eatSprouts()
            maze.eatSprouts()
        maze.clearAtPos(rat.getRow(), rat.getCol())
        rat.moveDown()
        maze.placeRat(rat.getChar(), rat.getRow(), rat.getCol())
    print (maze.toString())
    print (rat.toString())




def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, BASICFONT
    maze.placeRat('^', 4,1)
    print (maze.toString())
    drawMap(maze)

    while True:

        #thread 1 - look for an action
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                # Player clicked the "X" at the corner of the window.
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    moveRatRight()
                elif event.key == K_UP:
                    moveRatUp()
                elif event.key == K_LEFT:
                    moveRatLeft()   
                elif event.key == K_DOWN:
                    moveRatDown()                                  
                elif event.key == K_SPACE:
                    restart()
                else:
                    pass
            mapNeedsRedraw = True

        #thread 2: redraw the screen
        DISPLAYSURF.fill(BGCOLOR) #draws the turquoise background
        #if something has changed, redraw....
        if mapNeedsRedraw:
            mapSurf = drawMap(maze)
            mapNeedsRedraw = False

        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

        # Draw the map on the DISPLAYSURF object.
        DISPLAYSURF.blit(mapSurf, mapSurfRect)

        pygame.display.update() # draw DISPLAYSURF to the screen.
        FPSCLOCK.tick()

def drawMap(maze):
    #draw the tile sprites onto this surface.
    #this creates the visual map!
    mapSurfWidth = maze.getWidth() * TILEWIDTH
    mapSurfHeight = maze.getHeight() * TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(BGCOLOR)
    for h in range(maze.getHeight()):
        for w in range(maze.getWidth()):
            thisTile = pygame.Rect((w * TILEWIDTH, h * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
            if maze.getCharAtPos(h, w) in TILEMAPPING:
                #checks in the TILEMAPPING directory above to see if there is a
                #matching picture, then renders it
                baseTile = TILEMAPPING[maze.getCharAtPos(h,w)]

            # Draw the tiles for the map.
            mapSurf.blit(baseTile, thisTile)
    return mapSurf

def restart():
    maze.__init__()
    rat.setRow(4)
    rat.setCol(1)
    maze.placeRat(rat.getChar(), rat.getRow(), rat.getCol())
    drawMap(maze)

def terminate():
    #shutdown routine
    pygame.quit()
    sys.exit()



if __name__ == '__main__':
    main()

