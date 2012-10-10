multifind = []
txt = open("./extras/level02.txt", 'r')

for line in txt:
    for x in line:
        if x in multifind:
            continue
        else:
            multifind.append(x)
            print x
