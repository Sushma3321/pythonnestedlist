
paisa=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
crores=0
lakhs=0
rupee=0
while i<len(paisa):
    if paisa[i]>=10000000:
        crores=crores+1
    elif paisa[i]>=100000:
        lakhs=lakhs+1
    else:
        rupee=rupee+1
    i=i+1
print(crores)
print(lakhs)
print(rupee)


