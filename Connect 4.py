from pygame.locals import *
import pygame,os
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.display.set_caption("Connect 4")
screen = pygame.display.set_mode((780,780))
clock = pygame.time.Clock()
running = True
colors = [(255,255,255),(0,255,0),(255,0,0)]
squareslist = []
yourturn = 0
otherbutslist = []
font = pygame.font.Font('freesansbold.ttf', 32)
otherbutstext = []
otherbutsactions = []
win =0
ghoststatusrect = Rect(355,700,100,100)
statustext = "Game In Progress"
def boot():
    for i in range(7):
        squareslist.append([])
        for n in range (6):
            squareslist[i].append([])
            x = (i*100)+((i+1)*10)
            y = ((6-n)*100)+(( 6-n+1)*10)
            squareslist[i][n].append(Rect(x,y-110,100,100))
            squareslist[i][n].append(0)
    otherbutslist.append(Rect(10,700,200,50))
    otherbutsactions.append('reset()')
    otherbutstext.append('Reset')
def reset():
    global yourturn,statustext, win
    statustext = "Game In Progress"
    for i in range(7):
        for n in range(6):
            squareslist[i][n][1] = 0
    win = 0
    yourturn = 0
def checkwin(player):
    global win,statustext
    
    for i in range(7):
        counter = 0
        for n in range(6):
            if squareslist[i][n][1]==(player+1):
                counter+=1
            else:
                counter = 0
            if counter ==4:
                win =1 
    for i in range(6):
        counter = 0
        for n in range(7):
            if squareslist[n][i][1]==(player+1):
                counter+=1
            else:
                counter = 0
            if counter ==4:
                win =1
    for i in range(3):
        for n in range(4):
            counter = 0
            for p in range (4):
                if squareslist[n+p][i+p][1] ==(player+1):
                    counter+=1
    
                if counter == 4:
                    win = 1
    for i in range(3,6):
        for n in range(4):
            counter = 0
            for p in range (4):
                if squareslist[n+p][i-p][1] ==(player+1):
                    counter+=1
    
                if counter == 4:
                    win = 1
    if win == 1:
        statustext = "Player {} Won!".format(player+1)
boot()
    
while running:
    mouse = pygame.event.wait()
    if mouse.type ==MOUSEBUTTONDOWN and mouse.button==1:
        pos = pygame.mouse.get_pos()
        for i in range(7):
            if pos[0]>=squareslist[i][5][0].left and pos[0]<=squareslist[i][5][0].right and pos[1]>=squareslist[i][5][0].top and pos[1]<= squareslist[i][0][0].bottom and win ==0:
                hole = -1
                for n in range(6):
                    if squareslist[i][n][1] == 0:
                        hole = n
                        break
                if hole !=-1:
                    squareslist[i][hole][1] = yourturn+1
                    checkwin(yourturn)
                    if yourturn == 0:
                        yourturn = 1
                    else:
                        yourturn = 0
        for i in range(len(otherbutslist)):
            if pos[0]>=otherbutslist[i].left and pos[0]<=otherbutslist[i].right and pos[1]>=otherbutslist[i].top and pos[1]<= otherbutslist[i].bottom:
                exec(otherbutsactions[i])
    text = font.render(statustext,True,(0, 255, 0))
    screen.blit(text,ghoststatusrect)
    for i in range(7):
        for n in range (6):
            pygame.draw.rect(screen,colors[squareslist[i][n][1]],squareslist[i][n][0])
    for i in range(len(otherbutslist)):
        pygame.draw.rect(screen,(255,255,255),otherbutslist[i])
        text = font.render(otherbutstext[i],True,(0, 255, 0))
        screen.blit(text,otherbutslist[i])
    pygame.display.flip()
    screen.fill((0,0,0))
    clock.tick(60)
