# Напишите программу, которая принимает на вход цифру, обозначающую
# день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input('Enter the number of the day of the week: '))


def f_DayWeek(x):
    if x == 6 or x == 7:
        print(' - ', x, '-> ', 'yes, Weekend')
        return
    else:
        print(' - ', x, ' -> ', 'no')
        return


f_DayWeek(a)
