def IsSame(a1,a2,a3,x,y,z):
    if abs(a1-a2)==x and abs(a1-a3)==y and abs(a2-a3)==z:
        return True
    if abs(a1-a2)==x and abs(a1-a3)==z and abs(a2-a3)==y:
        return True
    if abs(a1-a2)==y and abs(a1-a3)==x and abs(a2-a3)==z:
        return True
    if abs(a1-a2)==y and abs(a1-a3)==z and abs(a2-a3)==x:
        return True
    if abs(a1-a2)==z and abs(a1-a3)==y and abs(a2-a3)==x:
        return True
    if abs(a1-a2)==z and abs(a1-a3)==x and abs(a2-a3)==y:
        return True
    return False
    

(x,y,z)=(int(x) for x in raw_input().split())
print x,y,z
Cr=0
Cy=0
Cb=0
ans=0
sequence=str()
sequence=list(x for x in raw_input())
print sequence
for i in range(len(sequence)):
    if sequence[i]=='R':
        Cr+=1
    elif sequence[i]=='Y':
        Cy+=1
    elif sequence[i]=='B':
        Cb+=1
    if IsSame(Cr,Cy,Cb,x,y,z):
        if ans < Cr+Cy+Cb:
            ans = Cr+Cb+Cy
        print 1111111
        Cr=0
        Cy=0
        Cb=0
    else:
        print 22222222
        if ans < Cr+Cy+Cb:
            ans = Cr+Cy+Cb
        
    print ans

