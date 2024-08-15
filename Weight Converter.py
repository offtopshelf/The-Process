#Create a program where the user inputs their weight in either lbs or kg it converts to the other

user_weight = int(input("Enter Weight: "))
unit = (input("(L)bs or (K)gs: "))


if unit.upper == 'l':
    convert = user_weight / 2.205
    print(str(convert) + "kgs")
elif unit.upper == 'k':
    convert = user_weight * 2.205
    print(str(convert) + "lbs")
else:
    print("Enter L or K.")