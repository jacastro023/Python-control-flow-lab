# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
a = int(input("enter side 1 of a triangle: "))
b = int(input("enter side 2 of a triangle: "))
c = int(input("enter side 3 of a triangle: "))
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
if a == b and c == a:
    triangle = "equalateral"
    print(f"A triangle with sides of {a}, {b} & {c} is a {triangle} triangle")
elif a == b or b == c or c == a:
    triangle = "isosceles"
    print(f"A triangle with sides of {a}, {b} & {c} is a {triangle} triangle")
else:
    triangle = "scalene"
    print(f"A triangle with sides of {a}, {b} & {c} is a {triangle} triangle")
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

# could not get it to work with sides being != as the second statement so had to switch the triangles around: the code would work but it would mark the statements for
# scalene and isosceles as both being scalene