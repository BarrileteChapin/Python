import sys

rows = int(sys.argv[1])
numbers = int(sys.argv[2])

#write 
fh = open(sys.argv[3],'r')


la = [] #list 

j =0 #line counter

p = 0 #incorrect answer 


for line in fh.readlines():
    la = line.split() 
    i=1
    j+=1
    for k in la:
        mul = j*i
        if(k!= str(mul)):
            p+=1
            print(f'{j} x   {i} = {k} is incorrect; should be {mul}')    
        i+=1

print(f'Multiplication table in file contains {p} errors')

fh.close()


