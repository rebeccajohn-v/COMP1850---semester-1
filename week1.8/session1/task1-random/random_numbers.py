import random

# Get user to input how many random numbers they want
nos = int(input("Enter how many random numbers you want: "))

# Generate this many random numbers
with open('random.txt','a') as file:
    for i in range(nos):
        random_num = random.randint(0,1000)
        file.append(random_num)


# Write the random numbers to a file named random.txt, one number per line
