####################################################################
with open('product.txt') as f:
    text=f.readlines()
f.close()
len_text = len(text)
####################################################################        
# Boyer Moore String Search implementation in Python
# Ameer Ayoub <ameer.ayoub@gmail.com>

# Generate the Bad Character Skip List
def generateBadCharShift(term):
    skipList = {}
    for i in range(0, len(term)-1):
        skipList[term[i]] = len(term)-i-1
    return skipList

# Generate the Good Suffix Skip List
def findSuffixPosition(badchar, suffix, full_term):
    for offset in range(1, len(full_term)+1)[::-1]:
        flag = True
        for suffix_index in range(0, len(suffix)):
            term_index = offset-len(suffix)-1+suffix_index
            if term_index < 0 or suffix[suffix_index] == full_term[term_index]:
                pass
            else:
                flag = False
        term_index = offset-len(suffix)-1
        if flag and (term_index <= 0 or full_term[term_index-1] != badchar):
            return len(full_term)-offset+1

def generateSuffixShift(key):
    skipList = {}
    buffer = ""
    for i in range(0, len(key)):
        skipList[len(buffer)] = findSuffixPosition(key[len(key)-1-i], buffer, key)
        buffer = key[len(key)-1-i] + buffer
    return skipList
    
# Actual Search Algorithm
def BMSearch(haystack, needle):
    goodSuffix = generateSuffixShift(needle)
    badChar = generateBadCharShift(needle)
    i = 0
    while i < len(haystack)-len(needle)+1:
        j = len(needle)
        while j > 0 and needle[j-1].lower() == haystack[i+j-1].lower():
            j -= 1
        if j > 0:
            badCharShift = badChar.get(haystack[i+j-1], len(needle))
            goodSuffixShift = goodSuffix[len(needle)-j]
            if badCharShift > goodSuffixShift:
                i += badCharShift
            else:
                i += goodSuffixShift
        else:
            return i
    return -1

####################################################################
# http://stackoverflow.com/questions/23049650/python-loop-of-radix-sort
def radixsort( aList ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1

  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]

    # split aList between lists
    for  i in aList:
      tmp = i // placement
##      print ("i is " , i)
##      print ("placement is " , placement)
##      print ("tmp is ", tmp)
##      print ("tmp % RADIX is ", tmp % RADIX)
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False

    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1

    # move to next digit
    placement *= RADIX
  return aList
######################################################################

while(1):
    print "Product Search - Input your 2 keyword (x for exit):"
    m= raw_input()
    if(m=='x'):
        break
    print "Product Enter Command-line Argument (Enter to default(10)):"
    o= raw_input()
    if(o==''):
        o=10
    j=1
    key=m.split()
    sort= [0]*(len_text-1)
    for i in range(0,len_text):
        a = BMSearch(text[i],key[0])   
        b = BMSearch(text[i],key[1])
        fn1=0
        fn2=0
        fn3=0
        if (a!=-1 or b!=-1):
            if(a!=-1):
                fn1+=20000000000
                fn2=+(99-a)*100000000
            if(b!=-1):
                fn1+=10000000000
                if(fn2==0):
                    fn2=+(99-b)*1000000
            if (a!=-1 and b!=-1):
                fn3=(99-abs(b-a))*10000
            fn=fn1+fn2+fn3+i
            #print j ,') ','line =',i,':',text[i] ,a,b,':',fn
            sort[j]=fn
            j+=1
    sort = [x for x in sort if x != 0]
    #print sort
    data_sort = radixsort(sort)
    #print data_sort
    for i in range(1,j):
        if(i>int(o)):
            break
        index = data_sort[len(data_sort)-i] % 10000
        print '-',text[index]
