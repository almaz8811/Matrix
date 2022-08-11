import sys, random, time

try:
    import bext, colorama
except ImportError:
    print('Для запуска программы нужны модули bext и colorama')
    sys.exit()

bext.title('Matrix')  # Поменять заголовок консольного окна
bext.clear()  # Очистить окно
bext.hide()  # Скрыть курсор
width, height = bext.size() # Получить размеры окна
width -= 1
height -= 1

# Константы цветов colorama
lgreen = colorama.Fore.LIGHTGREEN_EX
green = colorama.Fore.GREEN
