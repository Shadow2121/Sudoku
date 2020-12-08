import sudoku_che
import sudoku_drw
import pygame


def ai(arr, donotchange, win):
    while True:
        z = 0
        for i in range(9):
            dit = {}
            for j in range(9):
                if arr[i, j] == 0:
                    for t in range(1, 10):
                        sudoku_che.check(arr, i, j, t, win)
                        if arr[i,j] != 0:
                            dit[(i,j)] = t
                            arr[i][j] = 0
                            break
            rev_dict = {}   
            for key, value in dit.items(): 
                rev_dict.setdefault(value, set()).add(key) 
                
            result = [key for key, values in rev_dict.items() if len(values) > 1] 
            print(dit, result)
            
            for key,value in dit.items():
                if value not in result:
                    ii,jj = list(key)[0], list(key)[1]
                    arr[ii,jj] = value


            
        sudoku_drw.drow(win, arr, [0,0], donotchange, 0)

        ## Exit condition
        for i in range(9):
            for j in range(9):
                if arr[i,j] == 0:
                    z += 1
        if z == 0:
            break

        