import math
from cStringIO import StringIO

def infix(x,i):
##    print i,tree[(i*2)+1],tree[(i*2)+2]
    if(tree[(i*2)+1]=='+' or tree[(i*2)+1]=='-' or tree[(i*2)+1]=='*' or tree[(i*2)+1]=='/'):
        infix(x,(i*2)+1)
    else:
        if (tree[(i*2)+1]==0):
            tree[(i*2)+1]=x
        else:
            if (tree[(i*2)+2]==0):
                tree[(i*2)+2]=x
            else:
                infixR(x,(i-1)/2)


def infixR(x,i):
##    print i,tree[(i*2)+1],tree[(i*2)+2]
    if(tree[(i*2)+2]=='+' or tree[(i*2)+2]=='-' or tree[(i*2)+2]=='*' or tree[(i*2)+2]=='/'):
        infix(x,(i*2)+2)
    else:
        if (tree[(i*2)+1]== 0):
            tree[(i*2)+1]=x
        else:
            if (tree[(i*2)+2]== 0):
                tree[(i*2)+2]=x
            



def show_tree(tree, total_width=33, fill=' '):
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print output.getvalue()
    print '-' * total_width
    print
    return

print "Enter to input Postfix Expression : "
a= raw_input()
lena=len(a)
tree = [0]*15
stack=list(a)
tree[0]=stack[lena-1]
for k in range(2,lena+1):
    print stack[lena-k]
    if(stack[lena-k]=='+' or stack[lena-k]=='-' or stack[lena-k]=='*' or stack[lena-k]=='/'):
        infix(stack[lena-k],0)
    else:
        intnum =int(stack[lena-k])
        infix(intnum,0)
print tree
show_tree(tree)







                
