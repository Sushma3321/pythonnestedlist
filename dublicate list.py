n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
resultlist=[]
while i<=len(n):
    if i not in resultlist:
        resultlist.append(i)
    i=i+1
print(resultlist)


