
mainstr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
substr= "over"
a=mainstr.split()
i=0
while i<len(a):
    if "over" in a:
        a.remove("over")
    i=i+1
print(a)

mainstr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
substr= "over"
a=mainstr.replace("over","on")
print(a)




       


        



