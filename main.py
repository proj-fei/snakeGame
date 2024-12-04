import pygame
import random
from pygame.locals import *

PIXEL_SIZE = 20
APPLE_SIZE = (20, 20)
WINDOW_SIZE = (500, 500)
SNAKE_COLOR = (113, 74, 192)
FIELD_COLOR = (107, 142, 35)
APPLE_COLOR = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('SnakeGame')

def generate_apple(snake):
    max_x = WINDOW_SIZE[0] // PIXEL_SIZE
    max_y = WINDOW_SIZE[1] // PIXEL_SIZE

    while True:
        apple_x = random.randint(0, max_x - 1) * PIXEL_SIZE
        apple_y = random.randint(0, max_y - 1) * PIXEL_SIZE
        apple_pos = (apple_x, apple_y)

        if apple_pos not in snake:
            return apple_pos

snake_pos = [(240, 60), (260, 60), (280, 60), (300, 60), (320, 60)]
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_surface.fill(SNAKE_COLOR)
snake_direction = K_a

apple_pos = generate_apple(snake_pos)
apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
apple_surface.fill(APPLE_COLOR)
number_apple = 1
apple_cont = 0

background_image = pygame.image.load('assets/cena.png')
background_image = pygame.transform.scale(background_image, WINDOW_SIZE)

apple_image = pygame.image.load('assets/apple.png')
apple_image = pygame.transform.scale(apple_image, APPLE_SIZE)

while True:
    pygame.time.Clock().tick(5 + apple_cont * 0.2)
    screen.fill(FIELD_COLOR)
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if (event.key == K_w and snake_direction != K_s) or \
               (event.key == K_s and snake_direction != K_w) or \
               (event.key == K_a and snake_direction != K_d) or \
               (event.key == K_d and snake_direction != K_a):
                snake_direction = event.key

    next_head_pos = snake_pos[0]

    if snake_direction == K_w:
        next_head_pos = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direction == K_s:
        next_head_pos = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direction == K_a:
        next_head_pos = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
    elif snake_direction == K_d:
        next_head_pos = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])

    if next_head_pos in snake_pos or \
       next_head_pos[0] < 0 or next_head_pos[0] >= WINDOW_SIZE[0] or \
       next_head_pos[1] < 0 or next_head_pos[1] >= WINDOW_SIZE[1]:
        break

    for i in range(len(snake_pos) - 1, 0, -1):
        snake_pos[i] = snake_pos[i - 1]

    if next_head_pos == apple_pos:
        apple_cont += 1
        snake_pos.append(snake_pos[-1]) 
        apple_pos = generate_apple(snake_pos)

    snake_pos[0] = next_head_pos

    for pos in snake_pos:
        screen.blit(snake_surface, pos)

    screen.blit(apple_image, apple_pos)

    pygame.display.update()