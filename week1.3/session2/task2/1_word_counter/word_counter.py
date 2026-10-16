# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file

filename = input("Enter file name: ")

with open(filename,'r') as infile:
    file = [line for line in infile]


# calculate the number of words

words = []


for line in file:
    words.extend(line.split())


# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

print(len(words))

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210