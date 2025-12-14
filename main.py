import pygame
from matplotlib import colormaps
import numpy as np


COLOR_MAP = colormaps["coolwarm"]

BACKGROUND_OVERLAY_OFFSET = 10
GRID_OFFSET = 50
CELL_OFFSET = 10

WIDTH = 1920
HEIGHT = 1080

GRID_X = 10
GRID_Y = 6

GRID_SQUARE_WIDTH = 150
GRID_SQUARE_HEIGHT = 150

BLACK = (0, 0, 0)
BLUE = COLOR_MAP([0])[:, :3].squeeze() * 255
LIGHT_BLUE = (173, 216, 230)

print(BLUE)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


def draw_grid():
    grid_rect = pygame.Rect(
        GRID_OFFSET,
        GRID_OFFSET,
        GRID_SQUARE_WIDTH * GRID_X + CELL_OFFSET,
        GRID_SQUARE_HEIGHT * GRID_Y + CELL_OFFSET,
    )
    pygame.draw.rect(screen, LIGHT_BLUE, grid_rect)

    for i in range(GRID_X):
        for j in range(GRID_Y):
            cell_rect = pygame.Rect(
                GRID_OFFSET + CELL_OFFSET + i * GRID_SQUARE_WIDTH,
                GRID_OFFSET + CELL_OFFSET + j * GRID_SQUARE_HEIGHT,
                GRID_SQUARE_WIDTH - CELL_OFFSET,
                GRID_SQUARE_HEIGHT - CELL_OFFSET,
            )
            pygame.draw.rect(screen, BLUE, cell_rect)


def draw_background_overlay():
    background_overlay = pygame.Rect(
        BACKGROUND_OVERLAY_OFFSET,
        BACKGROUND_OVERLAY_OFFSET,
        WIDTH - 2 * BACKGROUND_OVERLAY_OFFSET,
        HEIGHT - 2 * BACKGROUND_OVERLAY_OFFSET,
    )
    pygame.draw.rect(screen, BLACK, background_overlay)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    screen.fill("white")

    # actual logic and stuff...
    draw_background_overlay()
    draw_grid()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
