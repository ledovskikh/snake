# snake.py
# Класс Snake для управления змейкой в игрr

import pygame
from settings import SNAKE_SIZE, WHITE, WINDOW_WIDTH, WINDOW_HEIGHT

class Snake:
    def __init__(self):
        self.length = 1  # Исходная длина змейки
        self.positions = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]  # Исходное положение змейки
        self.direction = pygame.K_RIGHT  # Исходное направление движения
        self.color = WHITE  # Цвет змейки

    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect((pos[0], pos[1]), (SNAKE_SIZE, SNAKE_SIZE))
            pygame.draw.rect(surface, self.color, rect)

    def move(self):
        cur = self.positions[0]
        x, y = cur
        if self.direction == pygame.K_UP:
            y -= SNAKE_SIZE
        elif self.direction == pygame.K_DOWN:
            y += SNAKE_SIZE
        elif self.direction == pygame.K_LEFT:
            x -= SNAKE_SIZE
        elif self.direction == pygame.K_RIGHT:
            x += SNAKE_SIZE
        new_head = (x, y)

        # Добавляем новую голову в начало списка
        self.positions = [new_head] + self.positions[:-1]

    def change_direction(self, direction):
        """Изменяет направление движения змейки, если новое направление не противоположно текущему."""
        if (direction == pygame.K_UP and self.direction != pygame.K_DOWN) or \
           (direction == pygame.K_DOWN and self.direction != pygame.K_UP) or \
           (direction == pygame.K_LEFT and self.direction != pygame.K_RIGHT) or \
           (direction == pygame.K_RIGHT and self.direction != pygame.K_LEFT):
            self.direction = direction

    def grow(self):
        """Увеличивает длину змейки, добавляя сегмент в её конец."""
        last = self.positions[-1]
        if self.direction == pygame.K_UP:
            self.positions.append((last[0], last[1] + SNAKE_SIZE))
        elif self.direction == pygame.K_DOWN:
            self.positions.append((last[0], last[1] - SNAKE_SIZE))
        elif self.direction == pygame.K_LEFT:
            self.positions.append((last[0] + SNAKE_SIZE, last[1]))
        elif self.direction == pygame.K_RIGHT:
            self.positions.append((last[0] - SNAKE_SIZE, last[1]))

    def check_collision(self):
        """Проверяет, столкнулась ли змейка с самой собой."""
        head = self.positions[0]
        return head in self.positions[1:]
