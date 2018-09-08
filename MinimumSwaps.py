#HackerRank Minimum Swaps 2
#Given unordered array of integers(without dulplicates), return minimum number of swaps required to sort the array in ascending order.



def minimumSwaps(arr):
    dup=sorted(arr)
    arrDict={}
    for i in range(len(arr)):
        arrDict[arr[i]]=i
    bookOfMap={}
    visited=[False]*len(arr)
    for i in range(len(arr)):
        if arr[i]!=dup[i]:
            bookOfMap[i]=arrDict[dup[i]]
        else:
            visited[i]=True
    result=0
    for j in range(len(arr)):
        if not visited[j]:
            cycle, tmp, on=False, 0, j
            while not cycle:
                if visited[on]:
                    cycle=True
                else:
                    visited[on]=True
                    on=bookOfMap[on]
                    tmp+=1
            result+=tmp-1
    return result
