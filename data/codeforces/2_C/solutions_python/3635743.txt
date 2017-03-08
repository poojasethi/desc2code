# coding=utf-8
"""
C. Задача комментатора
ограничение по времени на тест:1 second
ограничение по памяти на тест:64 megabytes
ввод:standard input
вывод:standard output

Олимпиада в Беркувере в самом разгаре. Здесь у каждого свои задачи — спортсмены борются за медали, а комментаторы за наиболее удобные места ведения репортажей. Сегодня основные спортивные мероприятия пройдут на трех круглых стадионах и задача комментатора выбрать оптимальную точку наблюдения, то есть такую из которой видны все три стадиона. Так как все состязания одинаково важны — то и стадионы должны быть видны из этой точки под одинаковым углом. Если таких точек несколько, то более предпочтительной является та, из которой угол обзора каждого стадиона максимален.

Помогите известному в Берляндии комментатору Г. Берниеву найти оптимальную точку наблюдения. Учтите, что стадионы не загораживают друг друга — комментатор может видеть легко наблюдать один стадион сквозь другой.
Входные данные

Входные данные состоят из трех строк, каждая из которых описывает положение одного стадиона. Строки имеют формат x, y, r, где (x,y) — это координаты центра стадиона ( - 103 ≤ x, y ≤ 103), а r (1 ≤ r ≤ 103) — это его радиус. Все числа во входных данных целые. Стадионы не пересекаются, а их центры не лежат на одной прямой.
Выходные данные

Выведите координаты искомой точки с пятью знаками после десятичной точки. Если решения не существует, то программа не должны выводить что либо. Иными словами она должны оставить выходные данные пустыми.
Примеры тестов
Входные данные
0 0 10
60 0 10
30 30 10
Выходные данные
30.00000 0.00000
"""
from sys import stdin
import math


def distance(x0, y0, v):
    x, y, r = v
    return math.sqrt((x - x0)**2 + (y - y0)**2) / r


def get_deviation(values):
    average = sum(values)/len(values)
    return math.sqrt(sum([(value - average)**2 for value in values])) / len(values)


def main():
    v1, v2, v3 = [(float(x), float(y), float(r)) for x, y, r in map(str.split, stdin.readlines())]
    x = sum([v[0] for v in [v1, v2, v3]])/3.0
    y = sum([v[1] for v in [v1, v2, v3]])/3.0
    e = 1e-7
    d = 1
    vertexes = [v1, v2, v3]
    current = get_deviation([distance(x, y, v) for v in vertexes])
    while True:
        x_p = get_deviation([distance(x + d, y, v) for v in vertexes])
        if x_p < current:
            current = x_p
            x += d
        else:
            x_m = get_deviation([distance(x - d, y, v) for v in vertexes])
            if x_m < current:
                current = x_m
                x -= d
            else:
                y_p = get_deviation([distance(x, y + d, v) for v in vertexes])
                if y_p < current:
                    current = y_p
                    y += d
                else:
                    y_m = get_deviation([distance(x, y - d, v) for v in vertexes])
                    if y_m < current:
                        current = y_m
                        y -= d
                    else:
                        d *= 0.7
        if d < e or current < e:
            break
    if current < 1e-5:
        print '{x:.5f}, {y:.5f}'.format(x=x, y=y)


main()
