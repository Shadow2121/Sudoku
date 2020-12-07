import pygame
import numpy as np
import sudoku_gen
import sudoku_che
import sudoku_drw
import sudoku_ai
import time

def main1():
    pygame.init()

    win = pygame.display.set_mode((800, 500))

    pygame.display.set_caption("SuDOku")

    arr = np.zeros((9,9), dtype=int)  ## Makng array of 9X9 to store the values
    donotchange = sudoku_gen.generate(arr)
    pos = [0, 0]

    start_time = time.time()
    ## MAIN GAME LOOP
    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x in range(500, 640) and y in range(400, 435):
                    run = False
                if x in range(500, 640) and y in range(350, 385):
                    sudoku_ai.ai(arr, donotchange, win)
            ## Movement of current block
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if pos[0] > 0:
                        pos[0] -= 1
                elif event.key == pygame.K_RIGHT:
                    if pos[0] < 8:
                        pos[0] += 1
                elif event.key == pygame.K_UP:
                    if pos[1] > 0:
                        pos[1] -= 1
                elif event.key == pygame.K_DOWN:
                    if pos[1] < 8:
                        pos[1] += 1
                else:
                    # print(event.key - 48)
                    if [pos[0], pos[1]] not in donotchange:
                        if (event.key - 48) in range(1, 10):
                            sudoku_che.check(arr, pos[1], pos[0], (event.key - 48), win)
                        if event.key == 32:      ## press space bar to remove the element(number)
                            arr[pos[1], pos[0]] = 0
                    else:   ## Displaying the worning message 
                        win.fill((0,0,0))
                        font = pygame.font.Font('freesansbold.ttf', 30)
                        text = font.render("You can not change that number", True, (255,0,0))  
                        win.blit(text,(10, 460))  
                        
        sudoku_drw.drow(win, arr, pos, donotchange, start_time)

    pygame.quit()

# main1()