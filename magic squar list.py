magic_square = [[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(magic_square):
    j=0
    c=0
    while j<len(magic_square[i]):
        a=magic_square[i][j]
        c=c+a
        j=j+1
    i=i+1
print("rows",c)
    
i=0
c1=0
while i<len(magic_square):
    b=magic_square[i][0]
    c1=c1+b
    i=i+1
print("rows",c1)

i=0
c2=0
while i<len(magic_square):
    b=magic_square[i][0]
    c2=c2+b
    i=i+1
print("column",c2)
i=0
c3=0
while i<len(magic_square):
    d=magic_square[i][2]
    c3=c3+d
    i=i+1
print("column",c3)

i=0
j=0
c4=0
while i<len(magic_square):
    h=magic_square[i][j]
    c4=c4+h
    j=j+1
    i=i+1
print("daigonals",c4)
i=0
j=2
c5=0
while i<len(magic_square):
    h1=magic_square[i][j]
    c5=c5+h1
    j=j-1
    i=i+1
print("diagonals",c5)
if c==c1==c2==c3==c4==c5:
    print("magicsquare")
else:
    print("not magic square")


    
    

    
    
    


    
    
    
    

