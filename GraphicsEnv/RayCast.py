import pygame
import math
from Orb import Orb

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Onscreen objects
orbs = [
    Orb((10, 20), 10, (255, 0, 0)),
        Orb((50, 80), 10, (255, 0, 0)),
        Orb((100, 150), 10, (255, 0, 0)),
        Orb((200, 250), 10, (255, 0, 0)),
        Orb((300, 350), 10, (255, 0, 0))
    ]

def draw():
    # Fill the screen with white color
    screen.fill(WHITE)
    
    # draw onscreen objects
    for orb in orbs:
            pygame.draw.circle(screen, orb.getColor(), orb.getPosition(), orb.getRadius())

def main():
    clock = pygame.time.Clock()  # To manage the frame rate
    running = True
    
    while running:
        # Handle events (like quitting)
        for event in pygame.event.get():
            # Closing the window
            if event.type == pygame.QUIT:
                running = False

        draw()  # Call the draw function to update the screen
        pygame.display.flip()  # Update the screen
        clock.tick(30)  # Cap the frame rate to 60 FPS

    pygame.quit()  # Quit pygame

if __name__ == "__main__":
    main()
