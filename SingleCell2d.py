import pygame
from Orb import Orb

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255) # Background color


# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orb Controller")

# Orb starting position (center of screen)
x, y = WIDTH // 2, HEIGHT // 2

orb = Orb((x,y))

# Main loop
running = True
while running:
    pygame.time.delay(15)  # Control speed of game loop

    # Check for events (like quitting)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move orb based on keys
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:   # Move left
        orb.changeX(-orb.getSpeed())
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Move right
        orb.changeX(orb.getSpeed())
    if keys[pygame.K_UP] or keys[pygame.K_w]:     # Move up
       orb.changeY(-orb.getSpeed())
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:   # Move down
        orb.changeY(orb.getSpeed())

    # Keep orb within screen boundaries
    orb.setX( max(orb.getRadius(), min(WIDTH - orb.getRadius(), orb.getX())))
    orb.setY(max(orb.getRadius(), min(HEIGHT - orb.getRadius(), orb.getY())))
    

    # Draw background and orb
    screen.fill(WHITE)
    pygame.draw.circle(screen, orb.getColor(), orb.getPosition(), orb.getRadius())

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
