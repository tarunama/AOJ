# -*- coding: utf-8 -*-


def ball(nums):
    l = []
    r = []
    for i, num in enumerate(nums):
        if i == 0:
            l.append(num)
        elif l[-1] < num:
            l.append(num)
        elif len(r) == 0:
            r.append(num)
        elif r[-1] < num:
            r.append(num)
        else:
            return 'NO'
    return 'YES'

N = int(input())


for _ in range(N):
    nums = [int(e) for e in input().split()]
    print(ball(nums))