# -*- coding: utf-8 -*-
"""
Problem Description
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A
"""


a = [e for e in input().split()]
l = []


for x in a:

    if x not in ['+', '-', '*']:
        x = int(x)
        l.append(x)
    else:
        a = l.pop()
        b = l.pop()

        if x == '+':
            l.append(b + a)
        elif x == '-':
            l.append(b - a)
        elif x == '*':
            l.append(b * a)


print(sum(l))
