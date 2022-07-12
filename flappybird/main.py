import pip
import pygame, sys, random
from pygame.locals import *

def draw_floor():
    display.blit(floor, (floor_x_pos, 650))
    display.blit(floor, (floor_x_pos + 432, 650))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos - 650))
    return bottom_pipe, top_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 706: # min height + pipe_height = 200 + 506
            display.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            display.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
        return False
    return True

def rotate_bird():
    pass

def bird_animation():
    pass

def score_display():
    pass

def update_score():
    pass

pygame.init()

display = pygame.display.set_mode((432, 768))
pygame.display.set_caption('Hello World')

# insert background
background = pygame.image.load('assests/background-night.png').convert()
background = pygame.transform.scale2x(background)

#insert floor 
floor_x_pos = 0
floor_HEIGHT = 224
floor_WIDTH = 432
floor = pygame.image.load('assests/floor.png').convert()
floor = pygame.transform.scale2x(floor)

#insert bird
bird = pygame.image.load('assests/yellowbird-midflap.png').convert()
bird = pygame.transform.scale2x(bird)

bird_rect = bird.get_rect(center = (100, 384))

#game variable
gravity = 0.25
bird_movement = 0
game_active = True

#create pipe
pipe_surface = pygame.image.load('assests/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_height = [200, 300, 400]
pipe_list = []

print(pipe_surface.get_height(), pipe_surface.get_width())

#create timer
spawn_pipe = pygame.USEREVENT
pygame.time.set_timer(spawn_pipe, 1200) # after 1200ms pipe will appear

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement = -11
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 384)
                bird_movement = 0  
        
        if event.type == spawn_pipe:
            pipe_list.extend(create_pipe())

    #draw background
    display.blit(background, (0, 0))

    if game_active:
        #draw bird
        bird_movement += gravity
        bird_rect.centery += bird_movement
        display.blit(bird, bird_rect)
        game_active = check_collision(pipe_list)

        #draw pipe
        pipe_list = move_pipe(pipe_list) 
        draw_pipe(pipe_list)  
    
    #draw floor
    draw_floor()

    floor_x_pos -= 1
    if floor_x_pos <= -floor_WIDTH:
        floor_x_pos = 0

    pygame.display.update()

pygame.quit()