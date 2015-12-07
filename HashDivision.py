print " Input (x for exit): "
m= raw_input()
n=m.split()
table=['']*50
if(len(n)<101):
    for i in range(0,len(n)):
        table[int(n[i]) % 50]+=n[i]
        table[int(n[i]) % 50]+=' '
    for i in range(0,50):
        print i, ' : ' ,table[i]
else:
    print 'Input over 100'
