import random

def generate(arr):
    ## temp code, any one have batter code change this (only file opening and reading part)
    all_q = []
    f = open("C:/Users/mihir/OneDrive/Documents/Sudoku/sudokus.txt")
    for i in f:
        # print(i)
        all_q = i.split(",")


    donotchange = []
    t = all_q[random.randrange(0, len(all_q))]
    c = 0
    for i in range(9):
        for j in range(9):
            arr[i][j] = t[c]
            if int(t[c]) != 0:
                donotchange.append([j,i])  ## Making array named donotchange that contain the boxes that should not be changed
            c += 1
    return donotchange
    