# -*- coding: utf-8 -*-


def solve():
    w = int(input())
    n = int(input())
    l = [i for i in range(1, w+1)]

    for _ in range(n):
        a, b = map(int, input().split(','))
        a -= 1
        b -= 1
        l[a], l[b] = l[b], l[a]

    print(*l, sep='\n')

solve()
