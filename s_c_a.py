# Write a code that works for all lists. It should print the output as the following like for all the odd numbers and all the even numbers and for all the numbers in the given list, it should calculate the following :
# count
# sum
# average


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
odd_count=0
even_count=0
sum1=0
sum2=0
count=0
while i<len(elements):
    count=count+1
    if elements[i]%2==0:
        even_count=even_count+1
        sum1=sum1+elements[i]
        avr1=sum1//even_count
    else:
        odd_count=odd_count+1
        sum2=sum2+elements[i]
        avr2=sum2//odd_count
    i=i+1
print(even_count)
print(odd_count)
print(sum1)
print(sum2)
print(count)
print(avr1)
print(avr2)





