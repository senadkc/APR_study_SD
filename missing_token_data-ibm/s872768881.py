a = [x + 1 for x in range(9)]
for i in a:
    j in a:
        print('%dx%d=%d'%(i, j, i * j))