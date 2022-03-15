import pygame
from planet import Planet
from settings import Settings
from pygame import mixer

pygame.init()
mixer.init()
settings = Settings()

SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.CAPTION)
mixer.music.load("space.ambience.mp3")
mixer.music.play(-1)
mixer.music.rewind()
mixer.music.set_volume(1)


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, settings.YELLOW, 1.98892 * 10 ** 30)
    sun.sun = True
    earth = Planet(-1 * Planet.AU, 0, 16, settings.BLUE, 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000
    mars = Planet(-1.524 * Planet.AU, 0, 12, settings.RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000
    mercury = Planet(0.387 * Planet.AU, 0, 8, settings.GREY, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000
    venus = Planet(0.723 * Planet.AU, 0, 14, settings.WHITE, 4.8673 * 10**24)
    venus.y_vel = -35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60)
        SCREEN.blit(settings.BG, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(SCREEN)

        pygame.display.update()

    pygame.quit()

main()
