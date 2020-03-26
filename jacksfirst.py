import pygame

pygame.init()

y_vel = -0.5
y_acc = 0.001
x = 275.0
y = 575.0

screen = pygame.display.set_mode((600, 600))

def drawToScreen():
    screen.fill((0, 0, 0))

    global y
    global y_vel
    global y_acc

    y += y_vel
    if(y >= 575.0 and y_vel > 0):
       y_vel *= -1
    y_vel += y_acc
    
    pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 25)
    pygame.display.update()

running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    drawToScreen()
    
pygame.quit()
