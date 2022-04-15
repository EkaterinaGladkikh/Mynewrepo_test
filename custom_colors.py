from colorama import Back

# Цвета для консоли
BLACK = '0'  # Чёрный
BLUE = '1'  # Синий
GREEN = '2'  # Зелёный
AQUA = '3'  # Голубой
RED = '4'  # Красный
PURPLE = '5'  # Лиловый
YELLOW = '6'  # Жёлтый
WHITE = '7'  # Белый
GRAY = '8'  # Серый
LIGHT_BLUE = '9'  # Светло-синий
LIGHT_GREEN = 'A'  # Светло-зелёный
LIGHT_AQUA = 'B'  # Светло-голубой
LIGHT_RED = 'C'  # Светло-красный
LIGHT_PURPLE = 'D'  # Светло-лиловый
LIGHT_YELLOW = 'E'  # Светло-жёлтый
VIVID_WHITE = 'F'  # Ярко-белый

BACK_CLR_BLACK = Back.BLACK + '   ' + Back.RESET
BACK_CLR_BLUE = Back.BLUE + '   ' + Back.RESET
BACK_CLR_CYAN = Back.CYAN + '   ' + Back.RESET
BACK_CLR_GREEN = Back.GREEN + '   ' + Back.RESET
BACK_CLR_MAGENTA = Back.MAGENTA + '   ' + Back.RESET
BACK_CLR_RED = Back.RED + '   ' + Back.RESET
BACK_CLR_WHITE = Back.WHITE + '   ' + Back.RESET
BACK_CLR_YELLOW = Back.YELLOW + '   ' + Back.RESET
BACK_CLR_LIGHTBLACK = Back.LIGHTBLACK_EX + '   ' + Back.RESET
BACK_CLR_LIGHTBLUE = Back.LIGHTBLUE_EX + '   ' + Back.RESET
BACK_CLR_LIGHTCYAN = Back.LIGHTCYAN_EX + '   ' + Back.RESET
BACK_CLR_LIGHTGREEN = Back.LIGHTGREEN_EX + '   ' + Back.RESET
BACK_CLR_LIGHTMAGENTA = Back.LIGHTMAGENTA_EX + '   ' + Back.RESET
BACK_CLR_LIGHTRED = Back.LIGHTRED_EX + '   ' + Back.RESET
BACK_CLR_LIGHTWHITE = Back.LIGHTWHITE_EX + '   ' + Back.RESET
BACK_CLR_LIGHTYELLOW = Back.LIGHTYELLOW_EX + '   ' + Back.RESET
BACK_CLR_RESET = Back.RESET

COLOR_CONSOLE = [BLACK, BLUE, GREEN, AQUA, RED, PURPLE, YELLOW, WHITE, GRAY, LIGHT_BLUE, LIGHT_GREEN, LIGHT_AQUA,
                 LIGHT_RED, LIGHT_PURPLE, LIGHT_YELLOW, VIVID_WHITE]

# CLR_COLOR = [BACK_CLR_BLACK, BACK_CLR_BLUE, BACK_CLR_CYAN, BACK_CLR_GREEN, BACK_CLR_MAGENTA, BACK_CLR_RED,
#              BACK_CLR_WHITE, BACK_CLR_YELLOW, BACK_CLR_LIGHTBLACK, BACK_CLR_LIGHTBLUE, BACK_CLR_LIGHTCYAN,
#              BACK_CLR_LIGHTGREEN, BACK_CLR_LIGHTMAGENTA, BACK_CLR_LIGHTRED, BACK_CLR_LIGHTWHITE, BACK_CLR_LIGHTYELLOW,
#              BACK_CLR_RESET]


COLOR_LIST = [i for i in range(0, 16)]
