from os import write
import sys

rows = int(sys.argv[1])
numbers = int(sys.argv[2])

#write 
fh = open(sys.argv[3],'w')


for j in range(1,rows+1):
    for i in range (1,numbers+1):
        mul = j*i
        print(f'{mul}')
        fh.write(f'{mul}')
        if(i != numbers): fh.write(' ');
        else: fh.write('\n');

fh.close()