#Take two lists, and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#Extras: 1.Randomly generate two lists to test this. 2.Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
import random
# Specify the range of numbers and the length of the lists
start_range = 1
end_range = 100
list_length = 12

# Generate the first list of random numbers
random_numbers_1 = [random.randint(start_range, end_range) for _ in range(list_length)]

# Generate the second list of random numbers
random_numbers_2 = [random.randint(start_range, end_range) for _ in range(list_length)]

print("First list:", random_numbers_1)
print("Second list:", random_numbers_2)

for overlap in random_numbers_1 and random_numbers_2:
    if overlap in random_numbers_1 and random_numbers_2:
        print(overlap)
    else:
        print("Error")


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for value in a and b:
    if value in a and b:
        print(value)
