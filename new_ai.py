
"""
It's gust back tracking algo
"""

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

def valid(temp_ans, i, j, key):
    ## Checking in row if the duplicate is there
    for q in range(9):
        if temp_ans[q][j] == key and q != i:
            return False  ## If duplicate is there then we can not insert the number
    ## Checking in column if the duplicate is there
    for q in range(9):
        if temp_ans[i][q] == key and q != j:
            return False  ## If duplicate is there then we can not insert the number
    ## Checking in 3X3 box if the duplicate is there
    for q in range((i // 3) * 3, ((i // 3) + 1) * 3):
        for z in range((j // 3) * 3, ((j // 3) + 1) * 3):
            if q == i and z == j:
                continue
            if temp_ans[q][z] == key:
                return False  ## If duplicate is there then we can not insert the number        
    return True

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, row, col, i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False
