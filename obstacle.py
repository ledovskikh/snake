class Obstacle:
    def __init__(self, position):
        self.position = position

    def draw(self, surface):
        rect = pygame.Rect(
            self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE
        )
        pygame.draw.rect(surface, pygame.Color("gray"), rect)
