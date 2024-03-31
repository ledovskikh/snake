import pygame
import sys
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, BLACK, BLUE


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.options = ["Начать игру", "Рекорды", "Выход"]
        self.selected_option = 0
        self.difficulties = ['Легкий', 'Средний', 'Сложный']
        self.selected_difficulty = 0  # Индекс выбранного уровня сложности

    def draw(self):
        self.screen.fill(BLACK)
        for i, option in enumerate(self.options):
            if i == self.selected_option:
                label = self.font.render(option, True, WHITE, BLUE)
            else:
                label = self.font.render(option, True, WHITE)
            self.screen.blit(label, (
                WINDOW_WIDTH // 2 - label.get_width() // 2, 200 + i * 50))

        pygame.display.update()

    def run(self):
        # Основной цикл меню
        while self.running:
            for event in pygame.event.get():
                # Обработка событий
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                    # Логика перемещения вверх по меню
                    elif event.key == pygame.K_DOWN:
                    # Логика перемещения вниз по меню
                    elif event.key == pygame.K_RETURN:
                        # Действие при выборе опции
                        if self.selected_option == 0:  # Если выбрана "Начать игру"
                            self.select_difficulty()
                        # Остальные опции

            self.draw()  # Отрисовка меню
            self.clock.tick(30)

    def select_difficulty(self):
        # Логика для выбора уровня сложности
        self.running = False  # Закрыть текущее меню
        difficulty_menu_running = True
        while difficulty_menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.selected_difficulty > 0:
                        self.selected_difficulty -= 1
                    elif event.key == pygame.K_DOWN and self.selected_difficulty < len(
                            self.difficulties) - 1:
                        self.selected_difficulty += 1
                    elif event.key == pygame.K_RETURN:
                        difficulty_menu_running = False  # Закрыть меню выбора сложности
            self.draw_difficulty_selection()  # Отрисовка меню выбора сложности

    def draw_difficulty_selection(self):
        # Отрисовка меню выбора уровня сложности
        self.screen.fill(BLACK)
        for i, difficulty in enumerate(self.difficulties):
            if i == self.selected_difficulty:
                label = self.font.render(difficulty, True, WHITE, BLUE)
            else:
                label = self.font.render(difficulty, True, WHITE)
            self.screen.blit(label, (
                WINDOW_WIDTH // 2 - label.get_width() // 2, 200 + i * 50))
        pygame.display.update()
