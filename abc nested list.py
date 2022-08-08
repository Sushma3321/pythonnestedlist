list=[["a","b","c"],["d","e","f"],["g","h","i"]]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        print(list[i][j],end=" ")
        j=j+1
    i=i+1