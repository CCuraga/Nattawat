def partition(A,p,r):
    i=p
    x=A[i]
    for j in range(p+1,r+1):
        if int(A[j])<=int(x):
            i=i+1
            exchange=A[j]
            A[j]=A[i]
            A[i]=exchange
    exchange2=A[p]
    A[p]=A[i]
    A[i]=exchange2
    return i

def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
    return A

output=''
print " Input : "
m= raw_input()
n=m.split()
if(len(n)<101):
    quicksort(n,0,(len(n)-1))
    sort=quicksort(n,0,(len(n)-1))
    for i in range(0,len(n)):
        output+=str(sort[i])
        output+=' '
    print output
else:
    print 'Input over 100'
    
