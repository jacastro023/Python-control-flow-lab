# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# set up initial point, need two numbers to start 0 and 1
# placeholder for incrementing the condition
a = 0
b = 1
i = 0
# while loop for only 50 numbers
while(i<51):
    print(f'term: {i} / number: {a}')
    a = b - a
    b = a + b
    i += 1
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
