#download input file 
#http://www.mediafire.com/download/glig343dkqqabnb/inputbp.txt
#http://www.mediafire.com/download/b815b1b270p9luj/inputbp2.txt
#http://www.mediafire.com/download/5z4v0zyh6ocxy38/inputbp3.txt

def ans(Bug,Time):
    global count 
    for i in range(0,numPatch):
        listPatch=list(Patch[i][1])
        check=0
        for j in range(0,numBug):
            if(listPatch[j]=='O' or listPatch[j]==Bug[j] ):
                check+=1
        if check==numBug:
            listoutput=list(Patch[i][2])
            outputbug=''
            for k in range(0,numBug):
                if(listoutput[k]=='O'):
                    outputbug+=Bug[k]
                elif(listoutput[k]=='+'):
                    outputbug+='+'
                elif(listoutput[k]=='-'):
                    outputbug+='-'
            flag=0
            for l in range(0,count):
                 if(table[l]==outputbug):
                    flag=1
                    if(tabletime[l]>=Time):
                        tabletime[l]=Time
            if flag==0:
                table[count]=outputbug
                tabletime[count]+=(int(Patch[i][0])+Time)
                count+=1
                ans(outputbug,tabletime[count-1])
    
with open('inputbp.txt') as f:
    text=f.readlines()
f.close()
len_text = len(text)    
line0=text[0].split()
numBug=int(line0[0])
numPatch=int(line0[1])
Patch=[0]*numPatch
Bug=''
table=[0]*(2**numBug)
tabletime=[0]*(2**numBug)

for i in range(0,numBug):
    Bug+='+'
for i in range(0,numPatch):
    Patch[i]=text[i+1].split()
    
table[0]=Bug
numtable=len(table)
count=1 
ans(Bug,0)
print table
print tabletime
for n in range(0,numtable):
    if(table[n]=='---'):
        print 'Fastest sequence takes %d seconds'%tabletime[n]
    elif (n+1==numtable):
        print' Bugs cannot be fixed'
