#HackerRank: Fraudulent Activity Notifications

def activityNotifications(expenditure, d):
    def find(rank):
        small=0
        for j in range(201):
            small+=count[j]
            if small>=rank:
                return j
        return -1         
    count=[0]*201
    for i in range(d):
        count[expenditure[i]]+=1
    ret=0
    if d&1:
        rank=(d+1)//2
        for i in range(d,len(expenditure)):
            if expenditure[i]>=(2*find(rank)):
                ret+=1
            count[expenditure[i-d]]-=1
            count[expenditure[i]]+=1
    else:
        rank1=d//2
        rank2=rank1+1
        for i in range(d,len(expenditure)):
            if expenditure[i]>=(find(rank1)+find(rank2)):
                ret+=1
            count[expenditure[i-d]]-=1
            count[expenditure[i]]+=1
    return ret 
