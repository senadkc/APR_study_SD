import sys 

for i in range(1, 10):
  for jrange(1, 10):
    sys.stdout.write("%dx%d=%d\n" % (i , j , i*j))