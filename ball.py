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

def draw(self):
        pygame.draw.rect(screen, OBJECT_COLOR, self.rect)

# Power-up class
class PowerUp:
    def __init__(self):
        x = random.randint(0, SCREEN_WIDTH - POWERUP_WIDTH)
        self.rect = pygame.Rect(x, 0, POWERUP_WIDTH, POWERUP_HEIGHT)

    def fall(self):
        self.rect.y += OBJECT_FALL_SPEED

    def draw(self):
        pygame.draw.rect(screen, POWERUP_COLOR, self.rect)

# Start screen
def show_start_screen():
    screen.fill(BACKGROUND_COLOR)
    title_font = pygame.font.Font(None, 74)
    title_text = title_font.render("Catch the Falling Objects", True, (0, 0, 0))
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 4))
    instructions_font = pygame.font.Font(None, 36)
    instructions_text = instructions_font.render("Press any key to start", True, (0, 0, 0))
    screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Game over screen
def show_game_over_screen(score, level, objects_caught, high_score):
    screen.fill(BACKGROUND_COLOR)
    game_over_font = pygame.font.Font(None, 74)
    game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 4))
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(f"Your Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    level_text = score_font.render(f"Level Reached: {level}", True, (0, 0, 0))
    screen.blit(level_text, (SCREEN_WIDTH // 2 - level_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))
    objects_text = score_font.render(f"Objects Caught: {objects_caught}", True, (0, 0, 0))
    screen.blit(objects_text, (SCREEN_WIDTH // 2 - objects_text.get_width() // 2, SCREEN_HEIGHT // 2 + 80))
    high_score_text = score_font.render(f"High Score: {high_score}", True, (0, 0, 0))
    screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 120))
    instructions_font = pygame.font.Font(None, 36)
    instructions_text = instructions_font.render("Press any key to restart", True, (0, 0, 0))
    screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, SCREEN_HEIGHT // 2 + 160))
    pygame.display.flip()

waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Pause screen
def show_pause_screen():
    pause_font = pygame.font.Font(None, 74)
    pause_text = pause_font.render("Paused", True, (0, 0, 0))
    screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

# Initialize game variables
basket = Basket()
objects = []
powerups = []
frame_count = 0
score = 0
level = 1
objects_caught = 0
high_score = 0
font = pygame.font.Font(None, 36)
game_over = False

# Main game loop
def main():
    global basket, objects, powerups, frame_count, score, level, objects_caught, high_score, game_over

    while True:
        # Start screen
        show_start_screen()
