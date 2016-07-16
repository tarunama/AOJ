# -*- coding:utf-8 -*-
import datetime


def main(a, b):
    dt = datetime.datetime(2004, a, b)
    week_num = dt.weekday()

    if week_num == 0:
        print('Monday')
    elif week_num == 1:
        print('Tuesday')
    elif week_num == 2:
        print('Wednesday')
    elif week_num == 3:
        print('Thursday')
    elif week_num == 4:
        print('Friday')
    elif week_num == 5:
        print('Saturday')
    elif week_num == 6:
        print('Sunday')


while True:
    a, b = [int(e) for e in input().split()]
    if a == 0 and b == 0:
        break

    main(a, b)
