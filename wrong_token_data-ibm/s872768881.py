a = [x + 1 for x im range(9)]
for i in a:
    for j in a:
        print('%dx%d=%d'%(i, j, i * j))