import pygame, sys, os
from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, player_width, player_height):
        super().__init__()
        self.rect = pygame.Rect(x, y, player_width, player_height)
        self.speedx = PLAYER_SPEED
        player_img = pygame.image.load(PLAYER_IMG).convert_alpha()
        surface = pygame.Surface((16, 16), pygame.SRCALPHA, 32)
        rect = pygame.Rect(0, 0, 16, 16)
        surface.blit(player_img, (0, 0), rect)
        self.sprite = pygame.transform.scale(surface, (160, 160))
    
    def draw(self,screen):
        # pygame.draw.rect(screen, BLUE, self.rect)
        screen.blit(self.sprite, (self.rect.x, self.rect.y))

    def movement(player):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT or pygame.K_d]:
            player.rect.x += player.speedx
        if keys[pygame.K_LEFT or pygame.K_a]:
            player.rect.x -= player.speedx

player = Player(100, 150, 150, 150)

while True:
    clock.tick(FPS)
    screen.fill((SKY_BLUE))
    player.movement()
    player.draw(screen)
    pygame.display.set_caption("超级马里奥 FPS: " + str(round(clock.get_fps(), 1)))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()