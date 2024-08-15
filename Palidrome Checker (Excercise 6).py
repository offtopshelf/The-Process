#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def define_palindrome():
    print("   Palindrome   ")
    print("noun. a word, phrase, or sequence that reads the same backward as forward")
 
def check_palindrome():
    user_word = str(input("Enter your word. "))
    palindrome = user_word[::-1]
    print(palindrome)
    if user_word == palindrome:
         print("This is a palindrome! ")
    else:
        print("This isn't a palindrome! ")

def main():
    is_running = True
    
        
    while is_running:
        print("Palindrome Checker")
        print("1.Define Palindrome")
        print("2.Check Palindrome")
        print("3.Exit")
        choice = input("Enter your choice (1-3). ")
        
        if choice == '1':
            define_palindrome()
        elif choice == '2':
            check_palindrome()
        elif choice == '3':
            is_running = False
        else:
            print("That is not an option!")


if __name__ == '__main__':
        main()
