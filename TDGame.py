# Import modules
import pygame


from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_a,
    K_s,
    K_w,
    K_d,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
score = 0 

current_path = os.path.dirname(__file__) # Where your .py file is located



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        global resource_path
        
        self.surf = pygame.Surface((75, 25))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 15)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self, player):
        self.rect.move_ip(-self.speed, 0)
        
        
running = True
