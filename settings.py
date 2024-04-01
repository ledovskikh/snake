# Размеры игрового окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Настройки змейки
SNAKE_SIZE = 20
SNAKE_SPEED = 1

# Настройки фруктов
FRUIT_SIZE = 20

# Настройки игры
FPS = 30  # Количество кадров в секунду

# Путь к файлу рекордов
RECORDS_FILE = "records.csv"

# Уровни
# DIFFICULTIES = {
#     'Легкий': {
#         'SNAKE_SPEED': 5,
#         'SPAWN_RATE': 5,
#         # С какой скоростью появляются новые препятствия/фрукты
#     },
#     'Средний': {
#         'SNAKE_SPEED': 10,
#         'SPAWN_RATE': 3,
#     },
#     'Сложный': {
#         'SNAKE_SPEED': 15,
#         'SPAWN_RATE': 1,
#     }
# }

DIFFICULTY_LEVELS = {
    "Легкий": {"speed": 5, "obstacles": 0},
    "Средний": {"speed": 10, "obstacles": 10},  # 10 препятствий
    "Сложный": {"speed": 15, "obstacles": 20},  # 20 препятствий
}
