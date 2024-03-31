# main.py
# Главный файл игры "Змейка" на PyGame, включающий в себя игровой цикл

import pygame
import sys
from snake import Snake
from fruit import Fruit
from menu import Menu
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, FPS, DIFFICULTIES


def load_menu(screen):
    menu = Menu(screen)
    menu.run()
    # Вернём выбранный уровень сложности
    return menu.selected_difficulty


def game_loop(screen, difficulty):
    # Здесь будет основной игровой цикл, с учётом выбранного уровня сложности
    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Змейка на PyGame")

    selected_difficulty = load_menu(screen)

    game_loop(screen, DIFFICULTIES[selected_difficulty])



if __name__ == "__main__":
    main()
