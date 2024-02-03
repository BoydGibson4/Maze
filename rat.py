#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Boyd Gibson
#
# Created:     03/11/2022
# Copyright:   (c) Boyd Gibson 2022
#-------------------------------------------------------------------------------

class Rat:
    #add rat attributes first!

    def __init__(self, x, r, c):
        """constructor for the rat.  Needs to pass in values
       for the character representing the rat, the row and the column
       >>>Rat("$", 2, 3)
       Nonetype"""
        self.char = x
        self.row = r
        self.col = c
        self.sprouts = 0

    def toString(self):
        info = "Rat " + self.char + " at row " + str(self.row) + " and column " + str(self.col)
        info = info +  " has eaten " + str(self.sprouts) + " sprouts today."
        return info

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getChar(self):
        return self.char

    def getSprouts(self):
        return self.sprouts

    def setRow(self, r):
        self.row = r

    def setCol(self, c):
        self.col = c

    def moveRight(self):
        self.col += 1

    def moveUp(self):
        self.row -=1

    def moveLeft(self):
        self.col -= 1

    def moveDown(self):
        self.row +=1

    def eatSprouts(self):
        self.sprouts += 1











