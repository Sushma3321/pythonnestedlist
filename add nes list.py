list=[[1,2,3],[4,5,6],[5,6,7]]
i=0
c=[]
while i<len(list):
    j=0
    s=0
    while j<len(list[i]):
        s=s+list[i][j]
        j=j+1
    c.append(s)
    j=0
    max=c[j]
    while j<len(c):
        if c[j]>max:
            max=c[j]
        j=j+1
    i=i+1
print(c)
print(max)








