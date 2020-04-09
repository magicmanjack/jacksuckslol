import pygame
import time

game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tile_width = 200
player_turn = 1 # player 1 always starts
white = (255, 255, 255)
green = (0, 255, 0)

txt_box_active = False
txt_box_active_color = (0, 150, 0)
txt_box_color = green
txt_box = pygame.Rect(100, 250, 400, 100)
txt_box_delay = 2
delay_start_time = time.time()

txt_box_input = u" "
out_code = u""


update_rate = 60 #Desired updates per second

order = int(input("Enter '1' or '2' to choose who goes first: "))
waiting = bool(order - 1)

pygame.init()

screen = pygame.display.set_mode((600, 600))

def turn_next():
    global player_turn
    global turns
    if player_turn == 1:
        player_turn = 2
    elif player_turn == 2:
        player_turn = 1

def draw_cross(x, y):
    global white
    pygame.draw.line(screen, white, (x, y), (x + tile_width, y + tile_width), 8)
    pygame.draw.line(screen, white, (x, y + tile_width), (x + tile_width, y), 8)
    
def draw_nought(x, y):
    global white
    pygame.draw.circle(screen, white, (x + tile_width // 2, y + tile_width // 2), tile_width // 2, 8)

def draw_grid():
    global white
    pygame.draw.line(screen, white, (200, 0), (200, 600), 8)
    pygame.draw.line(screen, white, (400, 0), (400, 600), 8)
    pygame.draw.line(screen, white, (0, 200), (600, 200), 8)
    pygame.draw.line(screen, white, (0, 400), (600, 400), 8)
    
def update():
    #all game updates are done in here
    global running
    global ms_x, ms_y
    global game_board
    global player_turn
    global waiting
    global delay_start_time
    global txt_box
    global txt_box_active
    global txt_box_color
    global txt_box_active_color
    global txt_box_input
    global txt_box_delay
    global green
    global out_code

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and txt_box_active:
            if event.key == pygame.K_RETURN:
                coordinates = txt_box_input.split("-")
                game_board[int(coordinates[0])][int(coordinates[1])] = player_turn
                txt_box_input = u""
                waiting = False
                txt_box_active = False
                txt_box_color = green
                turn_next()
            elif event.key == pygame.K_BACKSPACE:
                txt_box_input = txt_box_input[:-1]
            else:
                txt_box_input += event.unicode
            
    
    ms_x, ms_y = pygame.mouse.get_pos()
    
    
    if pygame.mouse.get_pressed()[0] and not game_board[int(ms_y / tile_width)][int(ms_x / tile_width)] and not waiting:
        game_board[int(ms_y / tile_width)][int(ms_x / tile_width)] = player_turn
        out_code = str(int(ms_y / tile_width)) + "-" + str(int(ms_x / tile_width))
        turn_next()
        waiting = True
        delay_start_time = time.time()
        
    elif pygame.mouse.get_pressed()[0] and time.time() - delay_start_time >= txt_box_delay:
        if txt_box.collidepoint(pygame.mouse.get_pos()):
            txt_box_active = True
            txt_box_color = txt_box_active_color
        else:
            txt_box_active = False
            txt_box_color = green


def render():
    #all game drawing is done in here
    global txt_box
    global txt_box_color
    global txt_box_active_color
    global txt_box_delay
    global txt_box_input
    global out_code
    
    for iy in range(0, 3):
        for ix in range(0, 3):
            if(game_board[iy][ix] == 1):
                draw_cross(ix * tile_width, iy * tile_width)
            elif(game_board[iy][ix] == 2):
                draw_nought(ix * tile_width, iy * tile_width)

    draw_grid()
    
    if waiting and time.time() - delay_start_time >= txt_box_delay:
        pygame.draw.rect(screen, txt_box_color, txt_box)
        line1 = pygame.font.Font(None, 32).render("Send this code to opponent: " + out_code, True, (0, 0, 0))
        line2 = pygame.font.Font(None, 32).render("Enter opponents code: " + txt_box_input, True, (0, 0, 0))
        screen.blit(line1, (txt_box.x + 10, txt_box.y + 10))
        screen.blit(line2, (txt_box.x + 10, txt_box.y + 50))
        
                
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
                
        
pygame.quit()
