def function(N,B,V,S):
    female=[[0 for i in range(B+1)]for j in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,B+1):
            female[i][j]=female[i-1][j]
            if j>=S[i-1]:
                female[i][j]=max(female[i-1][j], female[i-1][j-S[i-1]]+V[i-1])
    return female

def index(N,B,female,S):
    idx=[False for i in range(N)]
    j=B
    for i in range(N,0,-1):
        if female[i][j] > female[i-1][j]:
            idx[i-1]=True
            j-=S[i-1]
    return idx

(N,X,Y,B)=(int(x) for x in raw_input().split())
sf=[]
vf=[] 
sm=[] 
vm=[] 
ss=[] 
vv=[]
for n in range(N):
    (G,V,S)=(x for x in raw_input().split())
    S=int(S)
    V=int(V)
    if G=='F':
        sf.append(S)
        vf.append(V)
    if G=='M':
        sm.append(S)
        vm.append(V)
    ss.append(S)
    vv.append(V)
sumf=0
summ=0
for i in range(X):
    sumf+=sf[i]
bf=max(sumf,B)
for i in range(Y):
    summ+=sm[i]
bm=max(summ,B)
female=function(len(sf),bf,vf,sf)
male=function(len(sm),bm,vm,sm)
for i in range(len(female)):
    print female[i]
for i in range(len(male)):
    print male[i]
#print len(sf),len(sm)
indexfemale=index(len(sf),bf,female,sf)
indexmale=index(len(sm),bm,male,sm)
for i in range(X):
    if indexfemale[i]:
        print i+1
for i in range(Y):
    if indexmale[i]:
        print i+1
#ansv=0
#anss=0
#index0=0
#index1=0
#ans0=[]
#for i in range(B):
#    for j in range(B-i):
#        if ansv < female[X][i]+male[Y][j]:
#            ansv=female[X][i]+male[Y][j]
#            anss=i+j
#            indexfemale=index(X,i,female,sf)
#            indexmale=index(Y,j,male,sm)
#        if ansv == female[X][i]+male[Y][j] and anss > i+j:
#            anss = i+j
#            indexfemale=index(X,i,female,sf)
#            indexmale=index(Y,j,male,sm)
#        if ansv == female[X][i]+male[Y][j] and anss == i+j:
#            index0=index(X,i,female,sf)
#            index1=index(Y,j,male,sm)
#            if index0 > i:
#                indexfemale=index0
#                indexmale=index1
#            if index0 == i and index1>j:
#                indexfemale=index0
#                indexmale=index1
#
#for i in range(len(ss)):
#    for j in range(len(indexfemale)):
#        if indexfemale[j]:
#            if vv[i] == vf[j] and ss[i] == sf[j]:
#                ans0.append(i+1)
#    for j in range(len(indexmale)):
#        if indexmale[j]:
#            if vv[i] == vm[j] and ss[i] == sm[j]:
#                ans0.append(i+1)
#ans0.sort()
#ans=''
#print ansv,anss
#for i in range(len(ans0)):
#    ans+= str(ans0[i])+' '
#print ans
