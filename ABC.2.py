def trantotwo(a):
    b=str()
    a+='dd'
    for i in range(len(a)-2):
        if a[i]==a[i+1] and a[i]==a[i+2]:
            pass
        else:
            b+=a[i]
    return b

def twotrantonone(a):
    b=str()
    a+='d'
    for i in range(len(a)-1):
        if a[i]==a[i+1] or a[i]== a[i-1]:
            pass
        else:
            b+=a[i]
    return b
def isOne(a):
    for i in range(len(a)-1):
        if a[i]!=a[i+1]:
            return False
    return True
            


while True:
    try:
        a=raw_input()
        ans=0
        ans1=0
        y=trantotwo(a)
        x=str()
        while (len(x)!=len(y)):
            x=twotrantonone(y)
            z=y
            y=x
            x=z
#        print (str('x:')+x)
        if len(x)==0:
            ans = len(a)+1
        else:
            z=x
            z+='dd'
#            print (str('z:')+z)
            for i in range(len(z)-2):
#                print (i)
                if z[i]==z[i+2]:
                    y=z[:i+2]+z[i+1:-1]
#                    print (str('y:')+y)
                    x=str()
                    while (len(x)!=len(y)):
                        x=twotrantonone(y)
                        s=y
                        y=x
                        x=s
                    if len(x)==0:
                        ans1 = len(a)+1
                    else:
                        ans1 = len(a)-len(x)+1
                    if ans1 > ans:
                        ans=ans1
#                    print (ans)
                if i==len(z)-3 and ans < len(a)-len(z)+4:
#                    print (z[:-2])
                    ans = len(a)-len(z)+4
        print (ans)

    except EOFError:
        break
