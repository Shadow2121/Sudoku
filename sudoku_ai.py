import sudoku_che
import sudoku_drw
import pygame
import numpy as np



def ai(arr, donotchange, win):
    temp_ans = np.zeros((9,9), dtype=int)  ## Making temp array to store temp valus
    temp_ans_2 = np.zeros((9,9), dtype=int)  ## Making array with 0's and 1's in it to denote if we should enter that number

    mod = 0  ## Just variable to change starting value

    ## Main loop 
    while 1:
        z = 0  ## Variable that denotes the number of 0's in arr
        
        ## Setting values in temp_ans from arr that are in donotchange
        for i in range(9):
            for j in range(9):
                if [i,j] in donotchange:
                    temp_ans[j,i] = arr[j,i]

        ## Making temp prediction and writting it in temp_ans
        ## And making dict that will help us in placing the values
        for i in range(9):
            dit = {}
            for j in range(9):
                if arr[i, j] == 0:
                    for t in range((mod%9)+1, 10):
                        sudoku_che.check(arr, i, j, t, win)
                        if arr[i,j] != 0:
                            dit[(i,j)] = t
                            arr[i][j] = 0
                            break
            # print(dit)
            ## Putting values in temp_ans using dict
            for key, value in dit.items(): 
                temp_ans[list(key)[0], list(key)[1]] = value
        
        # print(temp_ans)

        ## Making temp_ans_2, if the value is unique then place 1 in temp_ans_2 in that palce using temp_ans
        for i in range(9):
            for j in range(9):
                temp = temp_ans[i,j]
                aa = sudoku_che.check_for_ai(temp_ans, i, j, temp_ans[i,j])
                if aa == 1:
                    temp_ans_2[j,i] = 1
                    temp_ans[i,j] = temp

        # print(temp_ans_2)

        ## Using temp_ans_2 writting ans to arr using temp_ans
        for i in range(9):
            for j in range(9):
                if temp_ans_2[j,i] == 1:
                    arr[i,j] = temp_ans[i,j]        
        # print(arr)

        ## Updating display
        sudoku_drw.drow(win, arr, [0,0], donotchange, 0)


        ## Exit condition
        for i in range(9):
            for j in range(9):
                if arr[i,j] == 0:
                    z += 1
        if z == 0:
            break

        mod += 1














































        # rev_dict = {}   
        # for key, value in dit.items(): 
        #     rev_dict.setdefault(value, set()).add(key) 
            
        # result = [key for key, values in rev_dict.items() if len(values) > 1] 

        # for key,value in dit.items():
        #     if value not in result:
        #         ii,jj = list(key)[0], list(key)[1]
        #         arr[ii,jj] = value