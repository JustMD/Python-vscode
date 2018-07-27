name1 = input("Name player 1 ? ")
name2 = input("Name player 2 ? ")
player1 = input( name1 + " choose: ")
player2 = input( name2 + " choose: ")

def compare(p1, p2) :
    a = "scizzors"
    b = "paper"
    c = "rock"
    if p1 == a and p2 == a:
        return " draw "
    elif p1 == a :
        if p2 == b : 
            return name1 + " wins"
        else :
            return name2 + " wins"
    elif p1 == b :
        if p2 == c : 
            return name1 + " wins"
        else :
            return name2 + " wins"
    elif p1 == c :
        if p2 == a : 
            return name1 + " wins"
        else :
            return name2 + " wins"    

print(compare(player1, player2))
