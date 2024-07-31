import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (135, 206, 235)

# Basket dimensions
BASKET_WIDTH = 200
BASKET_HEIGHT = 20
BASKET_COLOR = (139, 69, 19)

# Object dimensions
OBJECT_WIDTH = 30
OBJECT_HEIGHT = 30
OBJECT_COLOR = (255, 0, 0)

# Power-up dimensions
POWERUP_WIDTH = 30
POWERUP_HEIGHT = 30
POWERUP_COLOR = (0, 255, 0)

# Game settings
OBJECT_FALL_SPEED = 2
BASKET_SPEED = 10
NEW_OBJECT_INTERVAL = 30  # Frames
POWERUP_INTERVAL = 500  # Frames

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Load background music
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)

# Load sound effects
catch_sound = pygame.mixer.Sound("catch.wav")
game_over_sound = pygame.mixer.Sound("game_over.wav")
powerup_sound = pygame.mixer.Sound("powerup.wav")

# Basket class
class Basket:
    def __init__(self):
        self.rect = pygame.Rect((SCREEN_WIDTH - BASKET_WIDTH) // 2, SCREEN_HEIGHT - BASKET_HEIGHT - 10, BASKET_WIDTH, BASKET_HEIGHT)

    def move(self, dx):
        self.rect.x += dx
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - BASKET_WIDTH:
            self.rect.x = SCREEN_WIDTH - BASKET_WIDTH

    def draw(self):
        pygame.draw.rect(screen, BASKET_COLOR, self.rect)

# Object class
class FallingObject:
    def __init__(self):
        x = random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH)
        self.rect = pygame.Rect(x, 0, OBJECT_WIDTH, OBJECT_HEIGHT)

    def fall(self):
        self.rect.y += OBJECT_FALL_SPEED
