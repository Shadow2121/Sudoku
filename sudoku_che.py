import pygame

def check(arr, i, j, key, win):
    win.fill((0,0,0))
    caninsert = True
    ## Checking in row if the duplicate is there
    for q in range(9):
        if q == i:
            continue
        if arr[q][j] == key:
            # print("You can not enter this number here!!")
            font = pygame.font.Font('freesansbold.ttf', 30)
            text = font.render("You can not enter this number here!!", True, (255,0,0))  
            win.blit(text,(10, 460)) 
            caninsert = False  ## If duplicate is there then we can not insert the number
            break
    ## Checking in column if the duplicate is there
    for q in range(9):
        if q == j:
            continue
        if arr[i][q] == key:
            # print("You can not enter this number here!!")
            font = pygame.font.Font('freesansbold.ttf', 30)
            text = font.render("You can not enter this number here!!", True, (255,0,0))  
            win.blit(text,(10, 460)) 
            caninsert = False  ## If duplicate is there then we can not insert the number
            break
    ## Checking in 3X3 box if the duplicate is there
    for q in range((i // 3) * 3, ((i // 3) + 1) * 3):
        for z in range((j // 3) * 3, ((j // 3) + 1) * 3):
            if q == i and z == j:
                continue
            if arr[q][z] == key:
            #     print("You can not enter this number here!!")
                font = pygame.font.Font('freesansbold.ttf', 30)
                text = font.render("You can not enter this number here!!", True, (255,0,0))  
                win.blit(text,(10, 460))  
                caninsert = False  ## If duplicate is there then we can not insert the number
                break
    if caninsert == True:
        arr[i][j] = key


def check_for_ai(temp_ans, i, j, key):
    caninsert = True
    ## Checking in row if the duplicate is there
    for q in range(9):
        if q == i:
            continue
        if temp_ans[q][j] == key:
            caninsert = False  ## If duplicate is there then we can not insert the number
            break
    ## Checking in column if the duplicate is there
    for q in range(9):
        if q == j:
            continue
        if temp_ans[i][q] == key:
            caninsert = False  ## If duplicate is there then we can not insert the number
            break
    ## Checking in 3X3 box if the duplicate is there
    for q in range((i // 3) * 3, ((i // 3) + 1) * 3):
        for z in range((j // 3) * 3, ((j // 3) + 1) * 3):
            if q == i and z == j:
                continue
            if temp_ans[q][z] == key:
                caninsert = False  ## If duplicate is there then we can not insert the number
                break
    if caninsert == True:
        temp_ans[i][j] = key
        return 1
    else:
        return 0