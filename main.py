import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))

pygame.display.set_caption("SuDOku")

## DROW IN GAME WIN
def win_dr(win):
    pygame.draw.rect(win, (255,0,255), (0,0,450,450))  ## GAME BACKGROUND
    ## 4 LINES FOE DIVIDING THE MINE WIN
    pygame.draw.line(win, (0,0,0), (0,150), (450,150), 3)
    pygame.draw.line(win, (0,0,0), (0,300), (450,300), 3)
    pygame.draw.line(win, (0,0,0), (150,0), (150,450), 3)
    pygame.draw.line(win, (0,0,0), (300,0), (300,450), 3)

    ## MAKING EACH BOX
    # aadi
    pygame.draw.line(win, (0,0,0), (0,50), (450,50), 1)
    pygame.draw.line(win, (0,0,0), (0,100), (450,100), 1)
    pygame.draw.line(win, (0,0,0), (0,200), (450,200), 1)
    pygame.draw.line(win, (0,0,0), (0,250), (450,250), 1)
    pygame.draw.line(win, (0,0,0), (0,350), (450,350), 1)
    pygame.draw.line(win, (0,0,0), (0,400), (450,400), 1)
    # udhi
    pygame.draw.line(win, (0,0,0), (50,0), (50,450), 1)
    pygame.draw.line(win, (0,0,0), (100,0), (100,450), 1)
    pygame.draw.line(win, (0,0,0), (200,0), (200,450), 1)
    pygame.draw.line(win, (0,0,0), (250,0), (250,450), 1)
    pygame.draw.line(win, (0,0,0), (350,0), (350,450), 1)
    pygame.draw.line(win, (0,0,0), (400,0), (400,450), 1)

    pygame.display.update()


## MAIN GAME LOOP
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win_dr(win)

pygame.quit()