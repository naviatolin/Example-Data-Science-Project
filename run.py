# PREFACE: You do not need to comment this much normally; this is a tutorial and a way to have you ask me more questions on the basics of python 

# importing the 'numpy' library -> very commonly used in data science
import numpy

# importing the 'pandas' libary -> also very commonly used in data science
import pandas

# saving the filename as a string datatype to the variable 'filename'
filename = 'statistics.txt'
# print('1',filename)
# print('2',"filename")
# print('3',type(filename))

# using the pandas library to read a text file into something we can understand
dataframe = pandas.read_csv(filename)

# this is how the computer reads the text file
print("How read_csv works:")
print(dataframe)

# setting an intial value for a variable 'summation'
summation = 0
# print(type(summation))

# setting up an empty array called "highs"
highs = []

# "append" the avg_high column into a seperate array
highs.append(dataframe.avg_high)

# printing the 'highs' array
print("this is what appending does")
print(highs)

# 'for' loop that adds all of the 'highs' temperatures
for i in range(0,12):
  # what is i now: 2
  # showing how for loops work and iterations work in 'for' loops
  print("Counting: ", i)

  # recursively adding all of the temperatures together
  # the two brackets means the first column and the ith row
  summation = summation + highs[0][i]
  print("Summation: ", summation)

# lets try to answer this question
print("What do you think this number means?", int(summation/12))

# lets try to figure out what this section does together!

min = highs[0][0]

for i in range(0,12):
  if highs[0][i] < min:
    min = highs[0][i]
    
print("Printing whatever 'min' is: ")
print(min)