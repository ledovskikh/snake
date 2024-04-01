import pygame
import random
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FRUIT_SIZE, RED


class Fruit:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED  # Цвет фрукта
        self.randomize_position()

    def randomize_position(self):
        """Располагает фрукт в случайной позиции на игровом поле."""
        self.position = (
            random.randint(0, (WINDOW_WIDTH - FRUIT_SIZE) // FRUIT_SIZE)
            * FRUIT_SIZE,
            random.randint(0, (WINDOW_HEIGHT - FRUIT_SIZE) // FRUIT_SIZE)
            * FRUIT_SIZE,
        )

    def draw(self, surface):
        """Отрисовывает фрукт на переданной поверхности."""
        rect = pygame.Rect(
            (self.position[0], self.position[1]), (FRUIT_SIZE, FRUIT_SIZE)
        )
        pygame.draw.rect(surface, self.color, rect)
