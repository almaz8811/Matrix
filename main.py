import sys, random, time

try:
    import bext, colorama
except ImportError:
    print('Для запуска программы нужны модули bext и colorama')
    sys.exit()

class Drop:
    # Капли
    def __init__(self):
        self.x = random.randint(0, width)  # Начальное положение по горизонтали
        self.y = -1  # начальное положение по вертикали - за границей экрана
        self.drop_type = random.randint(0, 1)  # Тип: антикапля или капля
        self.timeout = random.randint(0, 3)  # Задержка до следующего перемещения
        self.wait_count = random.randint(0, 3)  # Счетчик паузы
    # Перемещение капель
    def move(self):
        if drop.wait_count < drop.timeout: # Пока рано перемещать
            drop.wait_count += 1 # Увеличить счетчик паузы
            return False
        else: # Можно перемещать
            drop.wait_count = 0 # Сбросить счетчик паузы
            drop.y += 1 # Переместить каплю или анти каплю на шаг вниз
            return True
    # Струйка
    def draw(self):
        if self.drop_type == 1:
            symbol = str(random.randint(1, 9))
            con_print(self.x, self.y, green, symbol)
            self.zero_draw() # Нарисовать яркий ноль
        else:
            con_print(self.x, self.y, green, ' ')
    # Ноль
    def zero_draw(self):
        if self.y < height:
            con_print(self.x, self.y + 1, lgreen, '0')
    # Перерождение капель
    def renew(self):
        self.__init__()

def is_rb_corner(x, y):
    if x == width and y == height:
        return True
    else:
        return False

def con_print(x, y, color, symbol):
    if not is_rb_corner(x, y):
        bext.goto(x, y)
        sys.stdout.write(color)
        print(symbol, end='')

bext.title('Matrix')  # Поменять заголовок консольного окна
bext.clear()  # Очистить окно
bext.hide()  # Скрыть курсор
width, height = bext.size()  # Получить размеры окна
width -= 1
height -= 1

# Константы цветов colorama
lgreen = colorama.Fore.LIGHTGREEN_EX
green = colorama.Fore.GREEN

# Массив капель и антикапель
drops = []
for i in range(1, width * 2 // 3):
    drop = Drop()
    drops.append(drop)

while True:
    for drop in drops:
        if drop.move(): # Проверить перемещение элемента
            drop.draw() # Показать элемент
            if drop.y >= height: # Элемент достиг дна
                drop.renew() # Обновить элемент
    key = bext.getKey(blocking=False) # Проверка нажатия клавиши
    if key == 'esc': # Если нажата ESC, выйти из программы
        bext.clear()
        sys.exit()
    time.sleep(0.02) # Задержка