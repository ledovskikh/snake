import pygame
import sys
import random
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from snake import Snake
from fruit import Fruit
from menu import Menu
from records import save_record
from settings import DIFFICULTY_LEVELS


def get_pause_menu_option_at_pos(mouse_pos, options, option_rects):
    """Определяет, на какую опцию меню кликнул пользователь."""
    for index, rect in enumerate(option_rects):
        if rect.collidepoint(mouse_pos):
            return options[index]
    return None


def draw_pause_screen(screen, selected_option):
    """Отображает экран паузы с опциями выбора."""
    screen.fill(BLACK)
    options = ["Продолжить", "Pfyjdj"]
    font = pygame.font.SysFont("arial", 48)
    for index, option in enumerate(options):
        text_color = (
            (255, 0, 0) if index == selected_option else (255, 255, 255)
        )
        pause_text = font.render(option, True, text_color)
        text_rect = pause_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + index * 60)
        )
        screen.blit(pause_text, text_rect)
    pygame.display.flip()


def show_final_screen(screen, score):
    screen.fill(BLACK)

    # Отображение текста "Game Over"
    font = pygame.font.SysFont("arial", 48)
    game_over_text = font.render("Game Over", True, (255, 255, 255))
    game_over_rect = game_over_text.get_rect(
        center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3)
    )
    screen.blit(game_over_text, game_over_rect)

    # Отображение счета игрока
    score_text = font.render(f"Ваш счет: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(
        center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    )
    screen.blit(score_text, score_rect)

    # Отображение кнопки "Выйти в меню"
    menu_text = font.render("Заново", True, (200, 200, 200))
    menu_rect = menu_text.get_rect(
        center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3 * 2)
    )
    screen.blit(menu_text, menu_rect)

    pygame.display.flip()

    # Ждем нажатия кнопки мыши или Enter для возврата в меню
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return "menu"  # Возвращаемся в меню
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu_rect.collidepoint(event.pos):
                    return "menu"  # Возвращаемся в меню


# def create_obstacles(level, width, height):
#     obstacles_count = DIFFICULTY_LEVELS[level]["obstacles"]
#     obstacles = []
#     for _ in range(obstacles_count):
#         # Генерируем случайную позицию для препятствия
#         pos_x = random.randint(0, width / SNAKE_SIZE - 1) * SNAKE_SIZE
#         pos_y = random.randint(0, height / SNAKE_SIZE - 1) * SNAKE_SIZE
#         obstacles.append(Obstacle((pos_x, pos_y)))
#     return obstacles


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Змейка")
    clock = pygame.time.Clock()

    menu = Menu(screen)
    game_state = "menu"
    pause_option_selected = 0

    while True:
        if game_state == "menu":
            snake = Snake()  # Инициализируем новую игру при выходе из меню
            fruit = Fruit()
            menu.run()  # Отобразить меню и ждать действия пользователя
            game_state = "playing"

        elif game_state == "playing":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = "paused"
                    else:
                        snake.change_direction(event.key)
                if snake.check_wall_collision(WINDOW_WIDTH, WINDOW_HEIGHT):
                    show_final_screen(screen, snake.score)
                    save_record(f"{menu.username}", snake.score)
                    game_state = "game_over"
                    continue

            snake.move()
            if snake.head_position() == fruit.position:
                snake.grow()
                fruit.randomize_position()

            screen.fill(BLACK)
            snake.draw(screen)
            fruit.draw(screen)
            pygame.display.flip()

        elif game_state == "paused":
            draw_pause_screen(screen, pause_option_selected)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        pause_option_selected = (
                            pause_option_selected + 1
                        ) % 2  # Переключение между опциями
                    elif event.key == pygame.K_RETURN:
                        if pause_option_selected == 0:  # Продолжить
                            game_state = "playing"
                        elif pause_option_selected == 1:  # Выйти в меню
                            save_record(
                                f"{menu.username}", snake.score
                            )  # Сохранить счёт перед выходом
                            game_state = "menu"

        elif game_state == "game_over":
            action = show_final_screen(
                screen, snake.score
            )  # Отображаем финальный экран и ждем действия пользователя
            if action == "menu":
                game_state = "menu"  # Переход обратно в начальное меню

        clock.tick(10 + 5 * DIFFICULTY_LEVELS[menu.selected_difficulty]["speed"])


if __name__ == "__main__":
    main()
