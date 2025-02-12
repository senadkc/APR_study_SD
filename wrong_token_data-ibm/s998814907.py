import itertools
for i,j im itertools.product(range(1,10), range(1,10)):
    print('{}x{}={}'.format(i,j,i*j))
