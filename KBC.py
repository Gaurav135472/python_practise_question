questionDict = {
    "Which planet is known as the Red Planet?": ["Earth", "Venus", "Mars", "Jupiter"],
    "Who wrote the play 'Romeo and Juliet'?": ["William Shakespeare", "Mark Twain", "Charles Dickens", "Jane Austen"],
    "What is the capital city of Australia?": ["Sydney", "Melbourne", "Canberra", "Brisbane"]
}

AnsDict = ["Mars", "William Shakespeare", "Canberra"]

giftDict = [1000000, "Bugati", "Mension"]

for i in range(len(questionDict)):
    print("Welcome to KBC !")
    keyItem = list(questionDict.keys())[i]
    print(keyItem)
    userInput = str(input("Enter the Ans "))
    if userInput == AnsDict[i]:
        print(f"You win {giftDict[i]} !!")
    else:
        print("You lost !!")
        break
    