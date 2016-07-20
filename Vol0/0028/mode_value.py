# -*- coding: utf-8 -*-

DICT = {k: 0 for k in range(1, 101)}


def solve(d):
    _max = max(d.values())
    for k, v in sorted(d.items()):
        if _max == v:
            print(k)

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            DICT[n] += 1
        except:
            break

    solve(DICT)




