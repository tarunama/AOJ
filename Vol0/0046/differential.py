# -*- coding: utf-8 -*-
l = []

while True:
    try:
        l.append(float(input()))
    except:
        break

_max = max(l)
_min = min(l)

print(_max - _min)
