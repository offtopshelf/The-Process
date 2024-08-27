

def greeting():
    print(f"***WELCOME***")
#Getting user's name
    userName = str(input("What's your name?: "))
    print(f"Greetings {userName}!\n Let's determine your grade!")
    

def gradingSystem():
    userGrade = int(input("Enter in your grade (0-100):"))
    print("")
#Letter Grades        
    if userGrade >= 90:
        print("A!")
    elif userGrade >= 80:
        print("B!")
    elif userGrade >= 70:
        print("C!")
    elif userGrade >= 60:
        print("D!")        
    else:
        print("F!")
        
#Message for gradingSystem        
    match userGrade:
        case userGrade if userGrade >= 90:
            print("Keep up the good work!")
        case userGrade if userGrade >= 80:
            print("You're doing great!")
        case userGrade if userGrade >= 70:
            print("Keep trying!")
        case userGrade if userGrade >= 60:
            print("We believe you can achieve more!")
        case _:
            print("We can do better together!")


#Arithmetic Operations
def miniCalculator():
    print("\nNow we can do some math for fun :)")
    print("\nWe will add two numbers then multiply by 4.")
    #(a+b)4 
    userNum1a = int(input("\nFirst number: "))
    userNum2a = int(input("Second number: "))
    print("\nThe answer is: ")
    print((userNum1a + userNum2a)*4)
    #(a+b+c)/3
    print("\nNow we will add three numbers then divide by 3.")
    userNum1b = int(input("First number: "))
    userNum2b = int(input("Second number: "))
    userNum3b = int(input("Third number: "))
    print("\nThe answer is: ")
    print(((userNum1b + userNum2b + userNum3b)//3))

def logic():
    print("\n")
    print("***   BEGIN CHAOS   ***")
    #Logical and Identity Opperations
    #and, or, not
    x = 999
    y = 666
    print(x > y and x == y)
    print(x >= y or x == y)
    print(not x + y == 0)
    #in, not in
    myList1 = [12, 23, 0, 2344, 1, 6]
    myList2 = [663, 666, 454, 23, 98]
    print(y not in myList1)
    print(x in myList2)
    #is, not 
    print(x is 666)
    print(y is not 3)
    
def looper():
#For/While Loops    
    x = 0
    y = range(11)
    
    while x <= 10:
        print(x)
        x += 1
    
    for i in y:
        print(i)
    print("***   END OF THE CHAOS   ***")
if __name__ == "__main__":
    greeting()            
    gradingSystem()
    miniCalculator()
    logic()
    looper()