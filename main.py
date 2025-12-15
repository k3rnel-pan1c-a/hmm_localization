import pygame
from matplotlib import colormaps
import numpy as np
from hmm import HMM

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

TIME_INCREMENT_BTN_WIDTH = 260
TIME_INCREMENT_BTN_HEIGHT = 75

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = COLOR_MAP([0])[:, :3].squeeze() * 255
LIGHT_BLUE = (173, 216, 230)

pygame.init()
pygame.display.set_caption("HMM-based robot localization")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()
running = True


TIME_INCREMENT_BTN_RECT = pygame.Rect(
    2 * GRID_OFFSET + GRID_SQUARE_WIDTH * GRID_X,
    GRID_OFFSET,
    TIME_INCREMENT_BTN_WIDTH,
    TIME_INCREMENT_BTN_HEIGHT,
)


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Grid:
    def __init__(self, grid_x, grid_y):
        self.cells = [[None for _ in range(grid_y)] for _ in range(grid_x)]


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


def draw_time_increment_button(mouse_pos):
    color = BLUE if TIME_INCREMENT_BTN_RECT.collidepoint(mouse_pos) else LIGHT_BLUE
    text_surf = font.render("TIME + 1", True, WHITE)
    text_rect = text_surf.get_rect(center=TIME_INCREMENT_BTN_RECT.center)
    pygame.draw.rect(screen, color, TIME_INCREMENT_BTN_RECT)
    screen.blit(text_surf, text_rect)


while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if TIME_INCREMENT_BTN_RECT.collidepoint(event.pos):
                print("button clicked...")

    screen.fill(WHITE)

    # actual logic and stuff...
    draw_background_overlay()
    draw_grid()
    draw_time_increment_button(mouse_pos)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
