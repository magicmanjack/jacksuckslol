import pygame
import time

update_rate = 60 #Desired updates per second

pygame.init()

screen = pygame.display.set_mode((600, 600))

#def update():
    #all game updates are done in here


#def render():
    #all game drawing is done in here
    

running = True
time_now = time.time_ns()
time_then = time_now
interval_time = 1000000000.0 / float(update_rate)
updates_queued = 0.0
updates = 0
frames = 0
can_render = False

print_time = time.time()

while(running):

    can_render = False
    
    time_now = time.time_ns()
    updates_queued += (time_now - time_then) / interval_time
    time_then = time_now

    while(updates_queued > 0):
        updates_queued-=1
        updates += 1
        #update()
        can_render = True

    if(can_render):
        screen.fill((0, 0, 0))
        #render()
        pygame.display.update()
        frames += 1

    if(time.time() - print_time >= 1):
        print_time += 1
        print("Updates:", updates, "\nFrames:", frames)
        updates = 0
        frames = 0

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
                
        
pygame.quit()
