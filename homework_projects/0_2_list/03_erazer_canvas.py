import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 4
GRID_COLS = WIDTH // CELL_SIZE
GRID_ROWS = HEIGHT // CELL_SIZE
ERASER_SIZE = 7

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canvas Eraser")
clock = pygame.time.Clock()

# Create grid (2D list representing cell colors)
grid = [[BLUE for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

# Eraser properties
eraser_active = False
eraser_rect = pygame.Rect(0, 0, ERASER_SIZE, ERASER_SIZE)

def draw_grid():
    """Draw the grid of cells"""
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, grid[row][col], rect)
            pygame.draw.rect(screen, BLACK, rect, 1)  # Grid lines

def apply_eraser():
    """Set all cells under the eraser to white"""
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if eraser_rect.colliderect(cell_rect):
                grid[row][col] = WHITE

def main():
    global eraser_active
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    eraser_active = True
                    eraser_rect.center = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    eraser_active = False
            elif event.type == pygame.MOUSEMOTION:
                if eraser_active:
                    eraser_rect.center = event.pos
                    apply_eraser()
        
        # Draw everything
        screen.fill(WHITE)
        draw_grid()
        
        # Draw eraser (semi-transparent)
        eraser_surface = pygame.Surface((ERASER_SIZE, ERASER_SIZE), pygame.SRCALPHA)
        pygame.draw.rect(eraser_surface, (*RED, 128), (0, 0, ERASER_SIZE, ERASER_SIZE))
        screen.blit(eraser_surface, eraser_rect)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()