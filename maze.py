#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Boyd Gibson
#
# Created:     03/11/2022
# Copyright:   (c) Boyd Gibson 2022
#-------------------------------------------------------------------------------

class Maze:
    """A 2D Maze"""

    def __init__(self):
        """The Maze constructor
        (none) -> none
        start by declaring attributes"""
        self.maze = [['#','#','#','#','#','#','#'],
                     ['#',' ','#',' ',' ',' ','#'],
                     ['#',' ','#',' ',' ',' ','#'],
                     ['#',' ',' ','@',' ','#','#'],      
                     ['#',' ','#',' ',' ',' ','#'],
                     ['#',' ','#',' ',' ',' ','#'],
                     ['#','#','#','#','#','#','#']]
        self.sprouts = 1
        self.height = 7
        self.width = 7

    def toString(self):
        printme = ""
        """for i in range (0, len(self.maze)):
            for j in self.maze[i]:
                printme = printme + j"""

        return printme

    def placeRat (self, rat_char, row, column):
        self.maze[row][column] = rat_char
                

    def clearAtPos(self, row, col):
        self.maze[row][col] = " "

    def eatSprouts(self):
        self.sprouts -= 1

    def goToLevel2(self):
        self.maze = [['#','#','#','#','#','#','#'],
                     ['#',' ','#',' ',' ','@','#'],
                     ['#',' ','#',' ',' ',' ','#'],
                     ['#',' ',' ','@',' ','#','#']
                     ['#',' ','#',' ',' ',' ','#'],
                     ['#',' ','#',' ',' ','@','#'],
                     ['#','#','#','#','#','#','#']]
        self.sprouts = 3

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getCharAtPos(self, row, col):
        return self.maze[row][col]
        
