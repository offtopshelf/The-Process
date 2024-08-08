#Program designed to ask the user for a number then respond if that number is even or odd

#getting user input
x = input("Give me a number please. ")
x = int(x)
#seeing if the input has a remainder or not 
if x % 2 == 0:
    print("Even")
#extra challenge 1 is it a multiple of 4
if x % 4 == 0:
    print("")
    print("It is also a multiple of 4")
elif x % 2 == 1:
    print("Odd")
    
#extra challenge 2 see if 2 inputs can divide into eachother
#getting inputs
print("")
print("Press enter to see if two numbers are factors of eachother....")
print(input())
y = input("1st number please.... ")
z = input("Now the 2nd....")
print("")
#daddy make him do the math
y = int(y)
z = int(z)
if y % z == 0:
    print("Yes they are!!!")
elif y % z != 0:
    print("No they are not!!!")
print("")
print(input("Goodbye!!!"))
