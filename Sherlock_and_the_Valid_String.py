# HackerRank: Sherlock and the Valid String

import collections
# Complete the isValid function below.
def isValid(s):
    book=collections.defaultdict(int)
    for ss in s:
        book[ss]+=1
    freq=collections.defaultdict(int)
    for b in book:
        freq[book[b]]+=1
    if len(freq)<2:
        return 'YES'
    if len(freq)>2:
        return 'NO'
    a,b=freq.keys()
    if b>a:
        a,b=b,a
    if (freq[a]==1 and a==b+1) or freq[b]==1:
        return 'YES'
    return 'NO'
