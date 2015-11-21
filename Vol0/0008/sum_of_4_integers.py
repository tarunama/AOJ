import sys
 
 
for n in sys.stdin:
    ret = 0
    for a in xrange(10):
        for b in xrange(10):
            for c in xrange(10):
                for d in xrange(10):
                    if a+b+c+d == int(n):
                        ret += 1
    print ret