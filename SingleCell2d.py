import pygame
from Orb import Orb

def handle_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

def move_orb():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:   # Move left
        main_orb.changeX(-main_orb.getSpeed())
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Move right
        main_orb.changeX(main_orb.getSpeed())
    if keys[pygame.K_UP] or keys[pygame.K_w]:     # Move up
        main_orb.changeY(-main_orb.getSpeed())
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:   # Move down
        main_orb.changeY(main_orb.getSpeed())

    # Keep main_orb within screen boundaries
    main_orb.setX(max(main_orb.getRadius(), min(WIDTH - main_orb.getRadius(), main_orb.getX())))
    main_orb.setY(max(main_orb.getRadius(), min(HEIGHT - main_orb.getRadius(), main_orb.getY())))

def draw():
    screen.fill(WHITE)
    # Draw main orb
    pygame.draw.circle(screen, main_orb.getColor(), main_orb.getPosition(), main_orb.getRadius())
    
    # Draw obstacles
    drawObstacles()
    
    # Update screen
    pygame.display.update()
    
def drawObstacles():
    orbs = [
        Orb((10, 20), 10, (255, 0, 0)),
        Orb((50, 80), 10, (255, 0, 0)),
        Orb((100, 150), 10, (255, 0, 0)),
        Orb((200, 250), 10, (255, 0, 0)),
        Orb((300, 350), 10, (255, 0, 0))
    ]
    for orb in orbs:
        pygame.draw.circle(screen, orb.getColor(), orb.getPosition(), orb.getRadius())


    

if __name__ == "__main__":
    
    # Initialize Pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 600, 400
    WHITE = (255, 255, 255)  # Background color

    # Create screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Orb Controller")

    # Orb starting position (center of screen)
    x, y = WIDTH // 2, HEIGHT // 2
    main_orb = Orb((x, y),20,(0, 0, 0))

    running = True
    

    while running:
        pygame.time.delay(15)
        handle_events()
        move_orb()
        draw()
    pygame.quit()
