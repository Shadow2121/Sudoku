import sudoku_che
import sudoku_drw
import pygame


def ai(arr, donotchange, win):    
    # for i in range(9):
    #     for j in range(9):
    #         if arr[i, j] == 0:
    #             for k in range(1,10):
    #                 sudoku_che.check(arr, i, j, k, win)
    #                 if arr[i, j] != 0:
    #                     break
    #             else:
    #                 print("lol")
    #                 j -= 1
    #                 while [i, j] not in donotchange and j > 0:
    #                     j -= 1
    #                     print(j)
    #                 for k in range(arr[i][j], 9):
    #                     sudoku_che.check(arr, i, j, k, win)
    #                     if arr[i, j] != 0:
    #                         break
    #             sudoku_drw.drow(win, arr, [0,0], donotchange, 0)

    ans = {}
    i,j = 0,0
    while i < 9:
        j = 0
        while j < 9:
            if arr[i, j] == 0:
                for k in range(1,10):
                    sudoku_che.check(arr, i, j, k, win)
                    if arr[i, j] != 0:
                        ans[(i,j)] = k
                        break
                else:
                    # print(list(ans)[-1])
                    i, j = list(list(ans)[-1])[0], list(list(ans)[-1])[1]
                    print(i, j)
                    ans.pop((i,j))
                    if arr[i, j] != 9:
                        arr[i, j] = 0
                        for k in range(arr[i, j]+1,10):
                            sudoku_che.check(arr, i, j, k, win)
                            if arr[i, j] != 0:
                                ans[(i,j)] = k
                                break
                    else:
                        print("lol")
            j += 1                
            sudoku_drw.drow(win, arr, [0,0], donotchange, 0)
        i += 1
    # print(ans)
