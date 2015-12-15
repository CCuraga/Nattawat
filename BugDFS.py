#download input file 
#http://www.mediafire.com/download/glig343dkqqabnb/inputbp.txt
#http://www.mediafire.com/download/b815b1b270p9luj/inputbp2.txt
#http://www.mediafire.com/download/5z4v0zyh6ocxy38/inputbp3.txt

with open('inputbp.txt') as f:
    text=f.readlines()
f.close()
len_text = len(text)    

line0=text[0].split()
numBug=int(line0[0])
numPatch=int(line0[1])
Patch=[0]*numPatch
Bug=''
tablemap=[0]*(2**numBug)
time=[0]*(2**numBug)

for i in range(0,numBug):
    Bug+='+'
for i in range(0,numPatch):
    Patch[i]=text[i+1].split()

tablemap[0]=Bug
numtablemap=len(tablemap)

global nummap  
nummap=1

def find(B,P):
    bug=list(B)
    patchlaw=list(P)
    j=0
    for i in range(0,numBug):
        if(patchlaw[i]=='O' or patchlaw[i]==bug[i] ):
            j+=1
    #print j
    if j==numBug:
        return 1
    else:
        return 0

def savemap(B,P,T):
    print B
    global nummap 
    bug=list(B)
    patchlaw=list(P)
    bugfix=''
    for i in range(0,numBug):
        if(patchlaw[i]=='O'):
            bugfix+=bug[i]
        elif(patchlaw[i]=='+'):
            bugfix+='+'
        elif(patchlaw[i]=='-'):
            bugfix+='-'
    j=0
    for i in range(0,numtablemap):
        if(tablemap[i]==bugfix):
            j+=1
            if time[i]>=T:   
                time[i]=T
    if j==0  :
        tablemap[nummap]= bugfix
        time[nummap]=T
        nummap+=1
        ans(bugfix,T)
        return bugfix,

def ans(B,T):
    for i in range(0,numPatch):
        if(find(B,Patch[i][1])):
           Bans=savemap(B,Patch[i][2],T+int(Patch[i][0]))
           print time,tablemap

def solve():    #Start Funtion
    ans(Bug,0)
    j=0
    for i in range(0,numtablemap):
        if(tablemap[i]=='---'):
            print'Shortest time %d'%time[i]
            j=1
    if j==0:
        print' Can not Fix Bug'
    
