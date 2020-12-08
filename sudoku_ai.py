import sudoku_che
import sudoku_drw
import pygame
import numpy as np



def ai(arr, donotchange, win):
    pass
#     temp_ans = np.zeros((9,9), dtype=int)
#     temp_ans_2 = np.zeros((9,9), dtype=int)

#     # dnc = donotchange.copy()
#     while 1:
#         z = 0
#         for i in range(9):
#             for j in range(9):
#                 if [i,j] in donotchange:
#                     temp_ans[j,i] = arr[j,i]

#         for i in range(9):
#             dit = {}
#             for j in range(9):
#                 if arr[i, j] == 0:
#                     for t in range(1, 10):
#                         sudoku_che.check(arr, i, j, t, win)
#                         if arr[i,j] != 0:
#                             dit[(i,j)] = t
#                             arr[i][j] = 0
#                             break
#             # print(dit)
#             for key, value in dit.items(): 
#                 temp_ans[list(key)[0], list(key)[1]] = value
        
#         print(temp_ans)

#         for i in range(9):
#             for j in range(9):
#                 # if [i,j] not in dnc:
#                 temp = temp_ans[i,j]
#                 aa = sudoku_che.check_for_ai(temp_ans, i, j, temp_ans[i,j])
#                 if aa == 1:
#                     temp_ans_2[j,i] = 1
#                     temp_ans[i,j] = temp

#         print(temp_ans_2)

#         for i in range(9):
#             for j in range(9):
#                 if temp_ans_2[j,i] == 1:
#                     arr[i,j] = temp_ans[i,j]
#                     # dnc.append([i,j])
        
#         # arr = temp_ans
#         # print(arr)

#         sudoku_drw.drow(win, arr, [0,0], donotchange, 0)


#         ## Exit condition
#         for i in range(9):
#             for j in range(9):
#                 if arr[i,j] == 0:
#                     z += 1
#         if z == 0:
#             break














































        # rev_dict = {}   
        # for key, value in dit.items(): 
        #     rev_dict.setdefault(value, set()).add(key) 
            
        # result = [key for key, values in rev_dict.items() if len(values) > 1] 

        # for key,value in dit.items():
        #     if value not in result:
        #         ii,jj = list(key)[0], list(key)[1]
        #         arr[ii,jj] = value