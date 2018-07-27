#palindrome = input("Insert a string to verify if it is a palindrome: ")
# palindrome = str(palindrome)
# rev = palindrome [::-1]
# if rev == palindrome :
#     print(palindrome + " is A Palindrome")
# else :
#     print("\"" + palindrome + "\" is NOT a Palindrome")


def reverse(word) :
    x = ''
    for i in range(len(word)) :
        x += word[::-1]
        return x

palindrome = input("Insert a string to verify if it is a palindrome:\n ")
x = reverse(palindrome)
if x == palindrome :
    print("is A Palindrome")
else :
    print("is NOT a Palindrome")