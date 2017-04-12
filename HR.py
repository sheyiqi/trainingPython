(N,X,Y,B)=(int(x) for x in raw_input().split())
female=[[0 for i in range(B+1)]for j in range(N+1)]
index_female==[[0 for i in range(B+1)]for j in range(N+1)]
male=[[0 for i in range(B+1)]for j in range(N+1)]
index_male==[[0 for i in range(B+1)]for j in range(N+1)]
value_female=0
sal_female=0
num_female=0
for i in range(N):
    (G,V,S)=(x for x in raw_input().split())
    S=int(S)
    V=int(V)
    sal_female+=S
    sal_female=min(sal_female,B)
    if G=='F':
        num_female+=1
        num_female=min(num_female,X)
        for j in range(num_female+1,1,-1):
            for k in range(sal_female,S,-1):
                if female[j-1][k-S]<0:
                    continue
                if female[j-1][k-S]+V>female[j][k]:
                    female[j][k]=female[j-1][k-S]+V
                    index_female=index_female[[j-1][k-S]
                    a=[]
                    a.append()
                    index_female[j][k]=a
