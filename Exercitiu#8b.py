print('''pick one:
            foarfece
            hartie
            piatra''')
print(" ")
print(" ")

while True:
    game_dict = {"piatra" : 1, "foarfece" : 2, "hartie" : 3}
    player1 = input("Player A: ")
    player2 = input("Player B: ")
    a = game_dict.get(player1)
    b = game_dict.get(player2)
    dif = a-b

    if dif in [-1, 2] :
        print("player A wins ")
        if input("Doriti sa mai incercati?, y sau n \n") == "y" :
            continue
        else:
            print("jocul s-a sfarsit")
            print(" ")
            break
    elif dif in [-2, 1] :
        print("player B wins")
        if input("Doriti sa mai incercati?, y sau n \n") == "y" :
            continue
        else:
            print("jocul s-a sfarsit")
            print(" ")
            break
    else :
        print("egalitate, mai incercati \n")
        print(" ")
        