#HackerRank: Frequency Queries


import collections
# Complete the freqQuery function below.
def freqQuery(queries):
    ret, content, freqNum=[], collections.defaultdict(int), collections.defaultdict(int)
    for q in queries:
        if q[0]==1:
            if freqNum[content[q[1]]]>0:
                freqNum[content[q[1]]]-=1
            content[q[1]]+=1
            freqNum[content[q[1]]]+=1
        elif q[0]==2:
            if content[q[1]]>0:
                freqNum[content[q[1]]]-=1
                content[q[1]]-=1
                freqNum[content[q[1]]]+=1
        else:
            if freqNum[q[1]]>0:
                ret.append(1)
            else:
                ret.append(0)
    return ret
