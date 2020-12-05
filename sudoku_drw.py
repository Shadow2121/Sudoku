import pygame
import time

def drow(win, arr, pos, donotchange, start_time):
    # win.fill((0,0,0))
    pygame.draw.rect(win, (255,255,255), (0,0,450,450))  ## GAME BACKGROUND
    
    ## High-lighting the boxes that user can not change
    for temp in donotchange:
        pygame.draw.rect(win, (105,105,105), (temp[0]*50,temp[1]*50,50,50))

    pygame.draw.rect(win, (0,0,0), (450,0,400,40)) 
    font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 20)
    text = font.render(str(time.time() - start_time), True, (0,255,0))  
    win.blit(text,(460, 10))

    font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 20)
    text = font.render("""Use arrow keys to move the box.""", True, (0,255,0))  
    win.blit(text,(460, 70))
    font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 20)
    text = font.render("""Use space bar to remove number.""", True, (0,255,0))  
    win.blit(text,(460, 100))

    ## 4 LINES FOE DIVIDING THE MINE WIN
    pygame.draw.line(win, (0,0,0), (0,150), (450,150), 3)
    pygame.draw.line(win, (0,0,0), (0,300), (450,300), 3)
    pygame.draw.line(win, (0,0,0), (150,0), (150,450), 3)
    pygame.draw.line(win, (0,0,0), (300,0), (300,450), 3)

    ## MAKING EACH BOX
    # rows
    pygame.draw.line(win, (0,0,0), (0,50), (450,50), 1)
    pygame.draw.line(win, (0,0,0), (0,100), (450,100), 1)
    pygame.draw.line(win, (0,0,0), (0,200), (450,200), 1)
    pygame.draw.line(win, (0,0,0), (0,250), (450,250), 1)
    pygame.draw.line(win, (0,0,0), (0,350), (450,350), 1)
    pygame.draw.line(win, (0,0,0), (0,400), (450,400), 1)
    # columns
    pygame.draw.line(win, (0,0,0), (50,0), (50,450), 1)
    pygame.draw.line(win, (0,0,0), (100,0), (100,450), 1)
    pygame.draw.line(win, (0,0,0), (200,0), (200,450), 1)
    pygame.draw.line(win, (0,0,0), (250,0), (250,450), 1)
    pygame.draw.line(win, (0,0,0), (350,0), (350,450), 1)
    pygame.draw.line(win, (0,0,0), (400,0), (400,450), 1)

    pygame.draw.rect(win, (255,0,0), (pos[0]*50,pos[1]*50,50,50), 2) ## High light the current block

    font = pygame.font.Font('freesansbold.ttf', 50)

    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:   ## do not print 0 in game
                continue
            text = font.render(str(arr[i][j]), True, (0,0,0))  ## Read the value fron arr
            win.blit(text,((j*50)+10, i*50))  ## printing the value to the game bord


    pygame.display.update()