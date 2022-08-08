# Occurences - is made from the word occur which means that how many times a certain character or word appears.
from re import M


list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
m=''.join(map(str,list))

l=str(m)
print(m)
i=0
b=[]
c=[]
count=0
while i<len(list):
      j=0
      count=0
      while j<len(l):
            if l[i]==l[j]:
                  count=count+1
            j=j+1
      b.append(l[i])
      if b not in b:
            b.append(count)
      i=i+1
print(b)
      

      
            





    


    

