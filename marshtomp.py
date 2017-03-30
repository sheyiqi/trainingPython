while True:
    try:
        line = list(i for i in raw_input().split())
        if len(line)==0:
            break
        for i in range(len(line)):
            if 'marshtomp' == line[i].lower():
                line[i] = 'fjxmlhx'
            if 'marshtomp' in line[i].lower():
                index = line[i].lower().find('marshtomp')
                line[i] = line[i][:index] + 'fjxmlhx' + line[i][index+9:]
        ans = str()
        for i in line:
            ans += str(i) + ' '
        print (ans)
    except EOFError:
        break
