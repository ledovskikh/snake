import pygame
import sys
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, BLACK, BLUE
from records import load_records, save_record


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 24)
        self.options = ["Начать игру", "Рекорды", "Выйти"]
        self.selected_option = 0
        self.username = ""
        self.difficulties = ["Легкий", "Средний", "Сложный"]
        self.selected_difficulty = "Легкий"
        self.option_rects = []

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.selected_option > 0:
                        self.selected_option -= 1
                    elif (
                        event.key == pygame.K_DOWN
                        and self.selected_option < len(self.options) - 1
                    ):
                        self.selected_option += 1
                    elif event.key == pygame.K_RETURN:
                        self.handle_option_selection()
                elif event.type == pygame.MOUSEMOTION:
                    # Обновляем выбранную опцию на основе положения курсора
                    for i, rect in enumerate(self.option_rects):
                        if rect.collidepoint(event.pos):
                            self.selected_option = i
                            break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Проверяем, было ли нажатие мыши в пределах одного из прямоугольников опций
                    for i, rect in enumerate(self.option_rects):
                        if rect.collidepoint(event.pos):
                            self.selected_option = i
                            self.handle_option_selection()
                            break
            self.draw()
            self.clock.tick(30)

    def handle_option_selection(self):
        if self.options[self.selected_option] == "Начать игру":

            self.input_username()
            self.select_difficulty()
            # Запуск игры
            print(
                f"Игра началась с именем пользователя {self.username} и сложностью {self.selected_difficulty}."
            )
            self.running = False
        elif self.options[self.selected_option] == "Рекорды":
            # Отображение таблицы рекордов
            self.show_records()
            # После просмотра рекордов пользователь может нажать любую клавишу, чтобы вернуться в меню
        elif self.options[self.selected_option] == "Выйти":
            # Выход из игры
            pygame.quit()
            sys.exit()

    def draw(self):
        self.screen.fill((0, 0, 0))  # Очистка экрана
        self.option_rects.clear()  # Очистка списка прямоугольников перед перерисовкой
        for index, option in enumerate(self.options):
            text = self.font.render(
                option,
                True,
                (
                    (255, 255, 0)
                    if index == self.selected_option
                    else (255, 255, 255)
                ),
            )
            text_rect = text.get_rect(
                center=(WINDOW_WIDTH // 2, 100 + 30 * index)
            )
            self.screen.blit(text, text_rect)
            self.option_rects.append(
                text_rect
            )  # Сохраняем прямоугольник для обработки клика мыши
        pygame.display.flip()

    def select_difficulty(self):
        selecting = True
        while selecting:
            self.screen.fill((0, 0, 0))
            for i, difficulty in enumerate(self.difficulties):
                if difficulty == self.selected_difficulty:
                    text_color = (255, 255, 0)
                else:
                    text_color = (255, 255, 255)
                difficulty_text = self.font.render(
                    difficulty, True, text_color
                )
                self.screen.blit(difficulty_text, (100, 100 + i * 30))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if (
                        event.key == pygame.K_UP
                        and self.difficulties.index(self.selected_difficulty)
                        > 0
                    ):
                        self.selected_difficulty = self.difficulties[
                            self.difficulties.index(self.selected_difficulty)
                            - 1
                        ]
                    elif (
                        event.key == pygame.K_DOWN
                        and self.difficulties.index(self.selected_difficulty)
                        < len(self.difficulties) - 1
                    ):
                        self.selected_difficulty = self.difficulties[
                            self.difficulties.index(self.selected_difficulty)
                            + 1
                        ]
                    elif event.key == pygame.K_RETURN:
                        selecting = False

    def draw_difficulty_selection(self):
        self.screen.fill(BLACK)
        for i, difficulty in enumerate(self.difficulties):
            if i == self.selected_difficulty:
                label = self.font.render(difficulty, True, WHITE, BLUE)
            else:
                label = self.font.render(difficulty, True, WHITE)
            self.screen.blit(
                label,
                (WINDOW_WIDTH // 2 - label.get_width() // 2, 200 + i * 50),
            )
        pygame.display.update()

    def input_username(self):
        self.username = ""
        self.screen.fill((0, 0, 0))
        prompt = self.font.render("Введите имя: ", True, (255, 255, 255))
        self.screen.blit(prompt, (100, 100))
        pygame.display.flip()

        collecting = True
        while collecting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and self.username:
                        collecting = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.username = self.username[:-1]
                    else:
                        self.username += event.unicode
                    self.screen.fill((0, 0, 0))
                    self.screen.blit(prompt, (100, 100))
                    name_surface = self.font.render(
                        self.username, True, (255, 255, 255)
                    )
                    self.screen.blit(name_surface, (100, 140))
                    pygame.display.flip()

    def show_records(self):
        records = load_records("records.csv")  # Загрузка рекордов
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont("arial", 24)
        title = font.render("Рекорды", True, (255, 255, 255))
        self.screen.blit(title, (100, 10))  # Отображаем заголовок

        for i, record in enumerate(records):
            text = f"{i + 1}. {record['username']}: {record['score']}"
            record_text = font.render(text, True, (255, 255, 255))
            self.screen.blit(record_text, (100, 50 + i * 30))

        pygame.display.flip()

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif (
                    event.type == pygame.KEYDOWN
                    or event.type == pygame.MOUSEBUTTONDOWN
                ):
                    # Закрыть экран рекордов при любом нажатии клавиши или клике мыши
                    waiting_for_input = False
