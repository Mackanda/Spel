import pygame
import random

# Skapa skärmen
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survivor.io Clone")

# Spelare
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5
player_color = (0, 255, 0)
player_radius = 15

# Fiender
enemies = []
enemy_radius = 10
enemy_speed = 2

# Huvudspel-loop
running = True
clock = pygame.time.Clock()

while running:
    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    player = pygame.draw.circle(win, player_color, (player_x, player_y), player_radius)

    if len(enemies) < 5:
        enemy_x = random.randint(0, WIDTH)
        enemy_y = random.randint(0, HEIGHT)
        enemies.append((enemy_x, enemy_y))

    for enemy in enemies:
        enemy_x, enemy_y = enemy
        pygame.draw.circle(win, (255, 0, 0), (enemy_x, enemy_y), enemy_radius)
        if player.colliderect(pygame.Rect(enemy_x - enemy_radius, enemy_y - enemy_radius, 2 * enemy_radius, 2 * enemy_radius)):
            enemies.remove(enemy)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
