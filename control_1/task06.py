class GasStation:
    # Конструктор, принимающий один параметр - ёмкость резервуара колонки
    def __init__(self, volume):
        self.volume = volume
        self.filled_volume = 0
    # Резервуар создаётся пустой

    # Залить в резервуар колонки n литров топлива
    # Если столько не влезает в резервуар - не заливать ничего, выбросить exception
    def fill(self, n):
        if n + self.filled_volume > self.volume:
            raise Exception("Not enough free volume inside")
        else:
            self.filled_volume += n

    # Заправиться, забрав при этом из резервура n литров топлива
    # Если столько нет в резервуаре - не забирать из резервуара ничего, выбросить exception
    def tank(self, n):
        if self.filled_volume - n < 0:
            raise Exception("Not enough volume to tank")
        else:
            self.filled_volume -= n

    # Запросить остаток топлива в резервуаре
    def get_limit(self):
        return self.filled_volume