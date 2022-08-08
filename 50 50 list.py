
question_list = ["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]
options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],["1.software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
answer_list=["3","4","1"] 
option_list2= [[ "1.Seven", "2.Eight"],[ "1.Chennai", "2.Delhi"],["1.software Engineering",  "2.Agriculture"]]
answers=["1","2","1"]
print("welcome to KBC game")
print("you have 50:50 life line also")
i=0
while i<len(question_list):
    print(i+1,question_list[i])
    j=0
    while j<len(options_list[i]):
        print(options_list[i][j])
        j=j+1
    answer=(input("enter the answer"))
    if answer==answer_list[i]:
       print("congrats your answer is right ")
    elif answer=="50:50":
        print(option_list2[i])
        user=input("enter answer")
        if user==answers[i]:
            print("your answer is right")
        else:
            print("wrong answer")
            break
    else:
        print("sorry wrong answer")
    i=i+1





