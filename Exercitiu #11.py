number = int(input("Enter a number to find out if it is prime or not: "))

a = [x for x in range(2, number) if number % x == 0]

def verify( num ) :
    if num > 1 :
        if len(a) == 0 :
            print(num, "este prim")
        else :
            print(num, "nu este prim")
    else :
        print(num, "nu este prim")

verify(number)

