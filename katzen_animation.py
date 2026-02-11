import pygame
import sys
import random

# Initialisiere Pygame
pygame.init()

# Setze Fenstergröße
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Süße Katze mit Briefumschlag")

# Farben
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 182, 193)

# Lade Bilder
cat_image = pygame.image.load('katze.png')  # Deine Katze
envelope_image = pygame.image.load('briefumschlag.png')  # Dein Briefumschlag
heart_image = pygame.image.load('herz.png')  # Herz-Bild
cinema_ticket_image = pygame.image.load('kino_ticket.png')  # Kino-Gutschein
dinner_image = pygame.image.load('abendessen.png')  # Abendessen

# Skalieren der Bilder auf passende Größe
cat_image = pygame.transform.scale(cat_image, (150, 150))
envelope_image = pygame.transform.scale(envelope_image, (100, 70))
heart_image = pygame.transform.scale(heart_image, (40, 40))
cinema_ticket_image = pygame.transform.scale(cinema_ticket_image, (100, 50))
dinner_image = pygame.transform.scale(dinner_image, (100, 50))

# Positionen
cat_x, cat_y = 300, 300
envelope_x, envelope_y = 350, 450
heart_positions = [(random.randint(50, 750), random.randint(50, 550)) for _ in range(10)]

# Animation Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hintergrund
    screen.fill(WHITE)

    # Zeichne Herzen
    for pos in heart_positions:
        screen.blit(heart_image, pos)

    # Zeichne Katze
    screen.blit(cat_image, (cat_x, cat_y))

    # Öffnender Briefumschlag (kann als Animation mit Bewegung dargestellt werden)
    if envelope_y > 300:
        envelope_y -= 1  # Bewegung nach oben (Briefumschlag öffnet sich)

    screen.blit(envelope_image, (envelope_x, envelope_y))

    # Wenn Briefumschlag geöffnet, zeige Kino-Gutschein und Abendessen
    if envelope_y <= 300:
        screen.blit(cinema_ticket_image, (envelope_x - 120, envelope_y - 50))
        screen.blit(dinner_image, (envelope_x + 50, envelope_y - 50))

    # Aktualisiere Display
    pygame.display.update()

    # Frame Rate
    pygame.time.Clock().tick(30)

# Beende Pygame
pygame.quit()
sys.exit()
