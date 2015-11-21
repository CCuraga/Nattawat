class contact(object):
    def __init__(self):
        self.name = ''
        self.len = 0
        self.number

i=1
p=[0]*5
for i in range (0,5):
    p[i]=contact

while(1):
    print "Input command (h for help):"
    m= raw_input()
    if(m=='i'):
        print 'Enterphone number'
        a= raw_input()
        lena=len(a)
        if(lena>10):
            print 'error long'
        elif(lena<10):
            print 'error short'
        elif(lena==10):
            print'Enter the parson id to append the phone or "n" for new person:'
            b= raw_input()
            if(b=='n'):
                print 'Enter the name (8 characters maximum):'
                name = raw_input()
                p[i].name = name
                p[i].number= list(a)
            
    if(m=='d'):
        print 'delete'
    if(m=='m'):
        print 'modify'
    if(m=='s'):
        print 'enter 3 digits to search:'
    if(m=='h'):
        print 'i - insert a phone number\nd - delete a phone number\nm - modify a phone number\ns - search\nx - exit program'
    if(m=='x'):
        break



    





        
