import pygame
import time

game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tile_width = 200
global white
white = (255, 255, 255)

update_rate = 60 #Desired updates per second

pygame.init()

screen = pygame.display.set_mode((600, 600))

def draw_cross(x, y):
    pygame.draw.line(screen, white, (x, y), (x + tile_width, y + tile_width), 8)
    pygame.draw.line(screen, white, (x, y + tile_width), (x + tile_width, y), 8)
    
def draw_nought(x, y):
    pygame.draw.circle(screen, white, (x + tile_width // 2, y + tile_width // 2), tile_width // 2, 8)

def draw_grid():
    pygame.draw.line(screen, white, (200, 0), (200, 600), 8)
    pygame.draw.line(screen, white, (400, 0), (400, 600), 8)
    pygame.draw.line(screen, white, (0, 200), (600, 200), 8)
    pygame.draw.line(screen, white, (0, 400), (600, 400), 8)
    
def update():
    #all game updates are done in here
    global ms_x, ms_y
    global game_board
    ms_x, ms_y = pygame.mouse.get_pos()
    if(pygame.mouse.get_pressed()[0]):
        game_board[int(ms_y / tile_width)][int(ms_x / tile_width)] = 1
    elif(pygame.mouse.get_pressed()[2]):
        game_board[int(ms_y / tile_width)][int(ms_x / tile_width)] = 2
    


def render():
    #all game drawing is done in here
    
    for iy in range(0, 3):
        for ix in range(0, 3):
            if(game_board[iy][ix] == 1):
                draw_cross(ix * tile_width, iy * tile_width)
            elif(game_board[iy][ix] == 2):
                draw_nought(ix * tile_width, iy * tile_width)

    draw_grid()
                
running = True
time_now = time.time_ns()
time_then = time_now
interval_time = 1000000000.0 / float(update_rate)
updates_queued = 0.0
#updates = 0
#frames = 0
can_render = False

print_time = time.time()

while(running):

    can_render = False
    
    time_now = time.time_ns()
    updates_queued += (time_now - time_then) / interval_time
    time_then = time_now

    while(updates_queued > 0):
        updates_queued-=1
        #updates += 1
        update()
        can_render = True

    if(can_render):
        screen.fill((0, 0, 0))
        render()
        pygame.display.update()
        #frames += 1

    #if(time.time() - print_time >= 1):
    #    print_time += 1
    #    print("Updates:", updates, "\nFrames:", frames)
    #    updates = 0
    #    frames = 0

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
                
        
pygame.quit()
