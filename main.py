import pygame
import sudoku_main

pygame.init()

win = pygame.display.set_mode((800, 500))

pygame.display.set_caption("SuDOku")

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            print(x,y)
            if x in range(330, 470) and y in range(400, 435):
                run = False
            if x in range(250, 550) and y in range(270, 370):
                print("start")
                sudoku_main.main1()

    ## Game Name
    font = pygame.font.Font('freesansbold.ttf', 100)
    text = font.render("SUDOKU", True, (255,255,255))  
    win.blit(text,(190, 100))  

    ## Start Button
    pygame.draw.rect(win, (255,255,255), (250,270,300,100))
    font = pygame.font.Font('freesansbold.ttf', 70)
    text = font.render("START", True, (0,0,0))  
    win.blit(text,(285, 290))

    ## Quit Button
    pygame.draw.rect(win, (255,255,255), (330,400,140,35))
    font = pygame.font.Font('freesansbold.ttf', 28)
    text = font.render("QUIT", True, (0,0,0))  
    win.blit(text,(366, 405))

    pygame.display.update()

pygame.quit()