import pygame

WIDTH = 640
HEIGHT = 420
FPS = 60
WHITE_COLOR = (255, 255, 255)
RED_COLOR =   (255, 0,   0)
GREEN_COLOR = (0,   255, 0)
BLUE_COLOR =  (0,   0,   255)
YELLOW_COLOR =  (255, 255, 51)

pygame.init()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
surface.fill(WHITE_COLOR)
pygame.display.set_caption("Первая программа на PyGame")
pygame.display.set_icon(pygame.image.load("rocket.png"))
# background_image = pygame.image.load("back.jpg")
# background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
# surface.blit(background_image, (0,0))
pygame.display.update()

size = 75
pygame.draw.rect(surface, RED_COLOR, (WIDTH//2 - size//2, HEIGHT//2 - size//2, size, size))
pygame.draw.rect(surface, YELLOW_COLOR, (WIDTH//2 - size, HEIGHT//2 - size, size*2, size*2), 5)
pygame.draw.rect(surface, BLUE_COLOR, (WIDTH//2-3, HEIGHT//2-3, 6, 6))

pygame.draw.line(surface, GREEN_COLOR, (200, 20), (350, 50), 5)
pygame.draw.aaline(surface, GREEN_COLOR, (200, 40), (350, 70), 5)

pygame.draw.polygon(surface, YELLOW_COLOR, [[450, 200], [580, 290], [350, 340]], 5)
pygame.draw.polygon(surface, RED_COLOR, [[150, 210], [180, 250], [90, 290], [30, 230]])
pygame.draw.polygon(surface, RED_COLOR, [[150, 310], [180, 350], [90, 390], [30, 330]], 3)

pygame.display.update()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)


