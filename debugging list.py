name = ["Savitri", "Phule", "26"]
# Ab hum iss list ko use karke poora naam (full name) print karna chaste hai
print(name[0]+name[1]+name[2])
# Code mei dekhiye naam theek se print kyu nahi ho raha

marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
total_marks = 0
i = 0
while i < len(marks):
       total_marks = total_marks + int(marks[i])
       i=i+1
print(total_marks)