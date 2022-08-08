list=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
sub_list=["h","i","j"]
list[2][1][2].append(sub_list)
print(list)

a=[1,2,3,4]
i=0
s=[]
b=0
while i<len(a):
    b=b+a[i]
    s.append(b)
    i=i+1
print(s)
