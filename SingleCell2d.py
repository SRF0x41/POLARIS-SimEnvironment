import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
ORB_RADIUS = 20
SPEED = 5
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orb Controller")

# Orb starting position (center of screen)
x, y = WIDTH // 2, HEIGHT // 2

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
        x -= SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Move right
        x += SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:     # Move up
        y -= SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:   # Move down
        y += SPEED

    # Keep orb within screen boundaries
    x = max(ORB_RADIUS, min(WIDTH - ORB_RADIUS, x))
    y = max(ORB_RADIUS, min(HEIGHT - ORB_RADIUS, y))

    # Draw background and orb
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (x, y), ORB_RADIUS)

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
