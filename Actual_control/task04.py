class Ball:
    # Конструктор, принимающий три параметра - координаты на плоскости и массу.
    def __init__(self, x, y, m):
        if m <= 0:
            raise BaseException("Cannot create a ball with negative mass")
        self.x = x
        self.y = y
        self.m = m
    # Координаты могут быть любые, а масса только положительная.
    # При попытке создать шарик с массой <= 0 должен выбрасываться exception.

    # Класс должен позволять получить значения координат и массы обращением к полям с именами x, y, m

    # Переместить шарик на dx вдоль оси OX и на dy вдоль оси OY
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
b = Ball(0.0, 0.0, 1.0)
print(b.x, b.y, b.m)
b.move(1.0, -1.0)
print(b.x, b.y, b.m)