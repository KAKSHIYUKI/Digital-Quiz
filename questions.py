score = 0

question_1 = input("where does milk usually come from ").strip().lower()
print()
answer_1 = "cows".lower()

if question_1 == answer_1:
    print("Congratulations you got it correct")
    score += 1
    print()

else:
    print("Sorry thats incorrect, make sure you answer with yes or no.")
score -= 1
print()

question_2 = input("how many colors are in the rainbow(answer in word form)").strip().lower()
print()
answer_2 = "seven".lower()


if question_2 == answer_2:
    print("Congratulations you got it correct")
    score += 1
    print()

else:
    print("Sorry thats incorrect, make sure you answer with yes or no.")
    score -= 1
    print()

question_3 = input("where does l&p come from").strip().lower()
print()
answer_3 = "Paeroa".lower()

if question_3 == answer_3:
    print("Congratulations you got it correct")
    score += 1
    print()

else:
    print("Sorry thats incorrect, make sure you answer with yes or no.")
    score -= 1
    print()

question_4 = input("Who owns L&p").strip().lower()
print()
answer_4 = "Coca cola".lower()

if question_4 == answer_4:
    print("Congratulations you got it correct")
    score += 1
    print()

else:
    print("Sorry thats incorrect, make sure you answer with yes or no.")
    score -= 1
    print()

question_5 = input("What is the third language of nz (not english or maori)").strip().lower()
print()
answer_5 = "sign language".lower()

if question_5 == answer_5:
    print("Congratulations you got it correct")
    score += 1
    print()

else:
    print("Sorry thats incorrect, make sure you answer with yes or no.")
    score -= 1
    print()

question_6 = input("What is the capital of nz").strip().lower()
print()
answer_6 = "Wellington".lower()

if question_6 == answer_6:
    print("Congratulations you got it correct")
    score += 1
    print()

else:
    print("Sorry thats incorrect, make sure you answer with yes or no.")
    score -= 1
    print()

question_7 = input("What does the slang 'scrap' mean").strip().lower()
print()
answer_7 = "Fight".lower()

if question_7 == answer_7:
    print("Congratulations you got it correct")
    score += 1
    print()

else:
    print("Sorry thats incorrect, make sure you answer with yes or no.")
    score -= 1
    print()

question_8 = input("what is the most well known all blacks breakfast cerial").strip().lower()
print()
answer_8 = "weet bix".lower()

if question_8 == answer_8:
    print("Congratulations you got it correct")
    score += 1
    print()

else:
    print("Sorry thats incorrect, make sure you answer with yes or no.")
    score -= 1
    print()

question_9 = input("who makes pineapple lumps").strip().lower()
print()
answer_9 = "pascall".lower()

if question_9 == answer_9:
    print("Congratulations you got it correct")
    score += 1
    print()

else:
    print("Sorry thats incorrect, make sure you answer with yes or no.")
    score -= 1
    print()

question_10 = input("What explorer found nz first ").strip().lower()

answer_10 = "Abel tasman".lower()

if question_10 == answer_10:
    print("Congratulations you got it correct")
    score += 1
    print()

else:
    print("Sorry thats incorrect, make sure you answer with yes or no.")
    score -= 1
    print()

print("Your total score was {}".format(score))
