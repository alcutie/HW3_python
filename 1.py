# создаем функцию с параметрами "horse" и "figure"
def can_eat(horse, figure):
    # две переменные, которые хранят расстояние от коня до фигуры по осям x y соответственно
    # ставим модуль, т.к. расстояние не может быть отрицательным
    walk_x = abs(horse[0] - figure[0])
    walk_y = abs(horse[1] - figure[1])
    # т.к конь ходит на два хода по одной оси и еще один по другой (буквой Г) то ставим условие:
    # если расстояние по осям 2 и 1 ИЛИ 1 и 2
    if (walk_x == 2 and walk_y == 1) or (walk_x == 1 and walk_y == 2):
        # то возвращаем значение True (может съесть)
        return True
    else:
        # иначе возвраащем значение False (не может съесть)
        return False
