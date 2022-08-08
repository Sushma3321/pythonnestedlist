list=["10","15","4","23","8"]
a=len(list)


i=0
while i<(a-1):
    j=0
    while j<(a-1):
        if list[i]<list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]
        j=j+1
    i=i+1 
print(list)






