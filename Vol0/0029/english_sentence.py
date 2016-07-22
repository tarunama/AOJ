# -*- coding: utf-8 -*-
from collections import defaultdict

d = defaultdict(int)
_input = input()

for word in _input.split():
    d[word] += 1

times = sorted(d.items(), key=lambda item: item[1], reverse=True)
lengths = sorted(d.items(), key=lambda item: len(item[0]), reverse=True)

print(times[0][0], end=' ')
print(lengths[0][0])

