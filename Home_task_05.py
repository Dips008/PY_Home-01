# Напишите программу, которая принимает на вход координаты двух
# точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
x1 = int(input('Enter the X coordinate of the first point :'))
y1 = int(input('Enter the Y coordinate of the first point:'))

x2 = int(input('Enter the X coordinate of the second point :'))
y2 = int(input('Enter the Y coordinate of the second point :'))

dist = round(math.sqrt((x2-x1)**2+(y2-y1)**2), 3)

print(' - A(', x1, ',', y1, '); B(', x2, ',', y2, ') -> ', dist)
