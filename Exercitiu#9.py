import random

number = random.randint(0, 9)
guess = 0
count = 0

while guess != number and guess != "exit" :
    guess = input("Ghiceste numarul cuprins intre 0-9: ")

    if guess == "exit" :
        break

    guess = int(guess)
    count += 1

    if (guess < number) :
        print("prea mic")
    elif (guess > number) :
        print("prea mare")
    else :
        print("ai ghicit, ti-au trebuit numai" , count, "incercari!!")
input()