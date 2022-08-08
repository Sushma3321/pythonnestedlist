question_list = ["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]
options_list = [["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["software Engineering", "Counseling", "Tourism", "Agriculture"]]
answer_list=["3","4","1"]
i=0
while i<len(question_list):
    print(question_list[i])
    answer=(input("enter the answer"))
    if answer==answer_list[i]:
       print("congrats your answer is right ")
    elif answer!=answer_list[i]:
        print("sorry wrong answer")
    else:
       print("sorry wrong answer")
    j=0
    while j<len(options_list[i]):
        print(j+1,options_list[i][j])
        j=j+1
    i=i+1


