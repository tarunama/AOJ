d = {'A': True, 'B': False, 'C': False}

while True:
    try:
        a, t = input().split(',')
        d[a], d[t] = d[t], d[a]
    except:
        for k, v in d.items():
            if v:
                print(k)
        break
