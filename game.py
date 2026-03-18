import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Block")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player (basket)
player_width, player_height = 80, 15
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 40
player_speed = 7

# Falling block
block_size = 20
block_x = random.randint(0, WIDTH - block_size)
block_y = 0
block_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move player with keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Move block down
    block_y += block_speed

    # Check if block caught
    if (player_y < block_y + block_size and
        player_x < block_x + block_size and
        player_x + player_width > block_x):
        score += 1
        block_y = 0
        block_x = random.randint(0, WIDTH - block_size)

    # If block misses player, reset
    if block_y > HEIGHT:
        block_y = 0
        block_x = random.randint(0, WIDTH - block_size)

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))  # player
    pygame.draw.rect(screen, RED, (block_x, block_y, block_size, block_size))          # block

    # Show score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)   # 60 FPS
