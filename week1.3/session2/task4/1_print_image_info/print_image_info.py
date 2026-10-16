# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.


# Read the file content

with open("../images/feep.pgm",'r') as infile:
    file = [line for line in infile]

# print image dimension (i.e., Dimensions: width x height pixels)

print(file[2])

# print max gray value (i.e., Max Gray Value: max_gray_value)
