while True:
    try:
        y=str()
        z=str()
        x=raw_input()
        x+='dd'
        for i in range(len(x)-2):
            if x[i]==x[i+1] and x[i]==x[i+2]:
                pass
            else:
                y+=x[i]
        y+='d'
        print (y)
        for i in range(len(y)-1):
            if y[i]==y[i+1] or y[i]==y[i-1]:
                pass
            else:
                z+=y[i]
        print (z)
        if len(z)==0:
            print (len(x)-1)
        else:
            z+='dd'
            for i in range(len(z)-2):
                if z[i]==z[i+2]:
                    y=z[:i+1]+z[i+1]+z[i+1:]
                    y+='d'
                    print (z)
                    print (y)
                    z=str()
                    for i in range(len(y)-1):
                        if y[i]==y[i+1] or y[i]==y[i-1]:
                            pass
                        else:
                            z+=y[i]
                    print (z)
                    print (len(x)-len(z))
                    break
            print (z)
            print (len(x)-len(z)+2)

    except EOFError:
        break
