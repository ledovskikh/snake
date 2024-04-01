import pygame
from settings import SNAKE_SIZE, WHITE, WINDOW_WIDTH, WINDOW_HEIGHT


class Snake:
    def __init__(self):
        self.positions = [
            (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        ]  # Змейка начинает в центре
        self.direction = (
            pygame.K_RIGHT
        )  # Начальное направление движения - вправо
        self.length = 1  # Исходная длина змейки
        self.score = 0  # Начальный счёт
        self.color = pygame.Color("green")  # Цвет змейки

    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect((pos[0], pos[1]), (SNAKE_SIZE, SNAKE_SIZE))
            pygame.draw.rect(surface, self.color, rect)

    def move(self):
        head_x, head_y = self.head_position()
        if self.direction == pygame.K_UP:
            new_head = (head_x, head_y - SNAKE_SIZE)
        elif self.direction == pygame.K_DOWN:
            new_head = (head_x, head_y + SNAKE_SIZE)
        elif self.direction == pygame.K_LEFT:
            new_head = (head_x - SNAKE_SIZE, head_y)
        elif self.direction == pygame.K_RIGHT:
            new_head = (head_x + SNAKE_SIZE, head_y)
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()

    def change_direction(self, key):
        opposite_directions = {
            pygame.K_UP: pygame.K_DOWN,
            pygame.K_DOWN: pygame.K_UP,
            pygame.K_LEFT: pygame.K_RIGHT,
            pygame.K_RIGHT: pygame.K_LEFT,
        }
        if (
            key in opposite_directions
            and key != opposite_directions[self.direction]
        ):
            self.direction = key

    def grow(self):
        self.length += 1
        self.score += 10

    def head_position(self):
        return self.positions[0]

    def check_self_collision(self):
        head = self.head_position()
        return head in self.positions[1:]

    def check_wall_collision(self, width, height):
        head_x, head_y = self.head_position()
        return head_x < 0 or head_x >= width or head_y < 0 or head_y >= height
