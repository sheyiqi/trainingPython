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
        print (a)
        y=trantotwo(a)
        x=str[]
        while (len(x)!=len(y)):
            x=twotrantonone(y)
            z=y
            y=x
            x=z
        if len(x)==0:
            print (len(a)+1)
        else:
            z=x
            z+='dd'
            for i in range(len(z)-2):
                if z[i]==z[i+2]:
                    y=z[:i+2]+z[i+1]+z[i+1:-1]
                    print (z)
                    print (y)
                    z=str()
                    while (len(x)!=len(y)):
                        x=twotrantonone(y)
                        z=y
                        y=x
                        x=z
                    if len(x)==0:
                        print (len(a)+1)
                    else:
                        print (len(a)-len(z))
                        break
        print (z)
        print (len(x)-len(z)+2)

    except EOFError:
        break
