#HackerRank: Max Array Sum

def maxSubsetSum(arr):
    l=len(arr)
    book=[0]*l
    book[0]=arr[0]
    book[1]=max(arr[0],arr[1])
    for i in range(2,l):
        book[i]=max(book[i-2], book[i-1], book[i-2]+arr[i], arr[i])
    return book[-1]
