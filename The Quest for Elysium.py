#Welcome Message
print("Welcome Player!")

#Character Creator
name = input("What's your name, adventurer? ")
age = input("How old are you? ")
age = int(age)
age = str(age)
gender = input("Are you a boy or a girl? ")
print("")

print("Welcome " + name + "! You are a very brave warrior! Especially brave at " + age +" years old. Not every " + gender + " is willing to put their lives on the line to save the world!")
print("")
print("")
print("")
print(input())
#The "plot" that i stole from chat gpt
print("The ultimate goal of finding Elysium could be to attain eternal bliss, enlightenment, ultimate fulfillment, or eternal power.")
print(input())
print("Elysium could be depicted as a mythical place of peace, beauty, and reward for the hero's journey through challenges and quests. The discovery of Elysium could symbolize the hero's ultimate achievement or realization of their deepest desires or aspirations.")
print("")
print("")
print(input())
print("In The Quest for Elysium you may encounter various challenges and obstacles that you need to overcome to reach Elysium. ")
print("")
print("")
print(input())
print("By Overcoming these feats with determination and stratergy you can navigate the obstacles in your quest and ultimately reach the fabled destination of Elysium.")
print("")
print("")
print("")
print(input())
print("How will you begin?")
print("Your home? A dungeon? or in The Whispering Forest? ")
#pick starting location
startlocation = input("Where? ")
if startlocation == "home":
    print("Your adventure starts in your house. You hear birds chirping.")
#house start
print(input())
print("You hear a knock at your door. What do you do?")
houseop1 = input("Check the chest or answer the door?")
if houseop1 == "check the chest" or "chest":
    print("Your belongings. You already know what's in the chest, " + name + "! Open the door!")
if houseop1 == "door" or "the door" or "open the door":
    print("Your childhood friend is at the door with a blank expression on his face. You noticed the large amount of blood on his clothes. ")
print(input())
print("Your friend extends his hand with a scroll in it as he collapses to the ground before you could react.")
print(input())
houseop2 = input("Read the scroll" + name + "?")
if houseop2 == "yes":
    print("This is where plot would go")
if houseop2 == "no":
    print("Before you could close the door. The soul snatching demons eat your face off. Your journey ends here at a sad" + age + "years old. You suck," + name)
if startlocation == "dungeon":
    print("You start in a dank dark cave. You can hear various moans coming from the darkness.")
if startlocation == "forest":
    print("You start in a quiet, shadowy forest. Every so often the silence is broken by the croak of a raven.")