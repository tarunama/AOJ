# -*- coding: utf-8 -*-


def main(a, b):
    hit = 0
    blow = 0

    for a_e, b_e in zip(a, b):
        if a_e == b_e:
            hit += 1
        elif a_e in b:
            blow += 1

    print(hit, blow, sep=' ')

while True:
    try:
        a = [int(e) for e in input().split()]
        b = [int(e) for e in input().split()]
    except:
        break

    main(a, b)
