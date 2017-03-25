# -*- coding: utf-8 -*-


def find_max_rec(lst, start, end):
    mid = (start + end) // 2
    if start == (end - 1):
        return lst[mid]
    else:
        l = find_max_rec(lst, start, mid)
        r = find_max_rec(lst, mid, end)
        max_m = max(r, l)
    return max_m


def main():
    lst   = [e for e in range(10)]
    start = 0
    end   = len(lst)
    return find_max_rec(lst, start, end)


print(main()) # 9
