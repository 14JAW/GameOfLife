from PIL import Image
import cv2
import numpy as np
import time
import math

global size
size = 60
global board
board = [[0 for y in range(size)] for x in range(size)]
global dead
dead = (0, 0, 0)
global live
live = (255, 255, 255)
class pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def pixelClicked(event, y, x, flags, param):
    # Click and drag mouse from start to stop in order to select path
    if event == cv2.EVENT_LBUTTONDOWN:
        #print (x, " ", y)
        if board[x][y] == 0:
            board[x][y] = 1
        else:
            board[x][y] = 0
        cv2.imshow('image', board2Image())

def startImage():
    board[10][10] = 1
    for each in getNeighbors(10, 10):
        board[each.x][each.y] = 1
    for each in getNeighbors(13, 10):
        board[each.x][each.y] = 1
    for each in getNeighbors(8, 10):
        board[each.x][each.y] = 1
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 600,600)
    cv2.setMouseCallback('image', pixelClicked)
    cv2.imshow('image', board2Image())
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 600,600)
    
def getNeighbors(x, y):
    neighbors = []
    for i in range(x-1, x+2):
        if i >= 0 and i < size:
            if (y - 1) >= 0 and (y - 1) < size:
                item = pixel(i, y - 1)
                neighbors.append(item)
            if (y + 1) >= 0 and (y + 1) < size:
                item = pixel(i, y + 1)
                neighbors.append(item)
            if i != x:
                item = pixel(i, y)
                neighbors.append(item)
    return neighbors

def numLiveAround(x, y):
    neighbors = getNeighbors(x, y)
    numLive = 0
    for each in neighbors:
        if board[each.x][each.y] == 1:
            numLive += 1
    return numLive

def upDateBoard():
    for i in range(0, size - 1):
        for j in range(0, size - 1):
            numLive = numLiveAround(i, j)
            if numLive < 2 or numLive > 3:
                board[i][j] = 0
            elif numLive == 3:
                board[i][j] = 1
def board2Image():
    image = np.zeros((size, size, 3), np.uint8)
    for x in range(0, size):
            for y in range(0, size):
                if board[x][y] == 0:
                    image[x][y] = dead
                else:
                    image[x][y] = live
    return image

def main():
    startImage()
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 600,600)
    while (True):        
        cv2.imshow('image', board2Image())
        upDateBoard()
        time.sleep(.5)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

main()


