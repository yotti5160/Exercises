#HackerRank: Special Palindrome Again

def substrCount(n, s):
    ret=n
    for i in range(n):
        count=1
        if 0<i<n-1 and s[i-1]==s[i+1]:
            tmp, count=s[i-1], 2
            while 0<=i-count and i+count<n:
                if s[i-count]==s[i+count]==tmp:
                    count+=1
                else:
                    break
        ret+=(count-1)
    for i in range(n-1):
        count=0
        if 0<=i<n-1 and s[i]==s[i+1]:
            tmp, count=s[i], 1
            while 0<=i-count and i+1+count<n:
                if s[i-count]==s[i+1+count]==tmp:
                    count+=1
                else:
                    break
        ret+=count
    return ret
