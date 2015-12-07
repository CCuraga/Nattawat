print " Input (x for exit): "
m= raw_input()
n=m.split()
table=['']*50
over1000=''
for i in range(0,len(n)):
    if int(n[i])>1000:
        over1000+=str(i+1)+' '  
if over1000=='':
    if(len(n)<101):
        for i in range(0,len(n)):
            table[int(n[i]) % 50]+=n[i]
            table[int(n[i]) % 50]+=' '
        for i in range(0,50):
            print i, ' : ' ,table[i]
    else:
        print 'Input over 100'
else:
    print 'Number over 1000 at ',over1000 

