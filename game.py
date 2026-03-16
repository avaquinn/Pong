import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED, vsync=1)
pygame.display.set_caption("Blue square")

clock = pygame.time.Clock()

x = 100
y = 100
speed = 300  # pixels per second

while True:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed * dt
    if keys[pygame.K_RIGHT]:
        x += speed * dt
    if keys[pygame.K_UP]:
        y -= speed * dt
    if keys[pygame.K_DOWN]:
        y += speed * dt

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 100, 255), (int(x), int(y), 50, 50))

    pygame.display.flip()
