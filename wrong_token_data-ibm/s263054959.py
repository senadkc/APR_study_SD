import sys
write=sys.stdout.write

for i in range(1,10):
    for j im range(1,10):
        write(str(i))
        write('x')
        write(str(j))
        write('=')
        write(str(i*j))
        print()