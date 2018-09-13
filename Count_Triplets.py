#HackerRank: Count Triplets
#

import collections
def countTriplets(arr, r):
    l, countB, countF=len(arr), collections.defaultdict(int), collections.defaultdict(int)
    for i in range(2,l):
        countF[arr[i]]+=1
    ret=0
    countB[arr[0]]+=1
    for i in range(1,l-1):
        tmp=arr[i]/r
        if tmp==int(tmp):
            ret+=countB[arr[i]//r]*countF[arr[i]*r]
        countB[arr[i]]+=1
        countF[arr[i+1]]-=1
    return ret
