# -*- coding: utf-8 -*-


def judge_class(s):
    if s <= 48.00:
        return 'light fly'
    elif 48.00 < s <= 51.00:
        return 'fly'
    elif 51.00 < s <= 54.00:
        return 'bantam'
    elif 54.00 < s <= 57.00:
        return 'feather'
    elif 57.00 < s <= 60.00:
        return 'light'
    elif 60.00 < s <= 64.00:
        return 'light welter'
    elif 64.00 < s <= 69.00:
        return 'welter'
    elif 69.00 < s <= 75.00:
        return 'light middle'
    elif 75.00 < s <= 81.00:
        return 'middle'
    elif 81.00 < s <= 91.00:
        return 'light heavy'
    elif 91.00 <= s:
        return 'heavy'


while True:
    try:
        weight = float(input())
        print(judge_class(weight))
    except:
        break
