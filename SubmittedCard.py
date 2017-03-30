times = int(raw_input())
for i in range(times):
    (N,M)=(int(N) for N in raw_input().split())
    num=list(int(day) for day in raw_input().split())
    if N==0:
        print 100
        continue
    if M >= N:
        print 100
        continue
    num.append(100) 
    num.insert(0,0)
#    print (num)
    diff = []
    for j in range(len(num)-M-1):
        diff.append( num[j+M+1]-num[j])
#    print (diff)
    print (max(diff)-1)
