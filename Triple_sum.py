#HackerRank: Triple sum

import bisect
def triplets(a, b, c):
    a=list(set(a))
    b=list(set(b))
    c=list(set(c))
    a.sort()
    b.sort()
    c.sort()
    ret=0
    for bb in b:
        ret+=bisect.bisect_right(a,bb)*bisect.bisect_right(c,bb)
    return ret
