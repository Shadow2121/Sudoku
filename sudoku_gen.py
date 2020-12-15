import random
import csv

def generate(arr):
    ## temp code, any one have batter code change this (only file opening and reading part)
    with open('sudoku.csv', 'r') as file:
        temp = random.randrange(1,1001)
        reader = csv.reader(file)
        temp_list = []
        for row in reader:
            temp_list.append(row)


    donotchange = []
    t = temp_list[temp][0]
    c = 0
    for i in range(9):
        for j in range(9):
            arr[i][j] = t[c]
            if int(t[c]) != 0:
                donotchange.append([j,i])  ## Making array named donotchange that contain the boxes that should not be changed
            c += 1
    return donotchange