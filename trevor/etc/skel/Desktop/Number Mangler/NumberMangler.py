from math import sqrt

# TREVOR'S NUMBER MANGLER
#
# (Work in progress.  Press the F5 key to run, or use the Run menu.)
# (If it asks you "OK to save?", press "OK.")

# Step 1: ask the user for a number to mangle
x = int(input("Number to mangle: "))

# Step 2: mangle the number!
x = x + 10
x = x * 3
x = 12 / x
x = x / 2
x = sqrt(x * x) # sqrt is the "square root" function
x = x % 100 # % is the "modulo" or "remainder": x % 100 is the remainder
            # when you divide x by 100
x = 2 * (x + 1)

# NOTE FROM YICHEN:
# "This number mangler is stupid."
# "It has to work for all numbers, and it's not working for some of them."
# "Take out the line that's breaking things.  The rest is fine."

# Note from me: if you want to take out a line of code without deleting it,
# put a # symbol in front of it instead.  Lines that start with a # symbol
# are ignored by the computer.

# Second note from me: Yichen's right, but she could have said that a lot more
# nicely.
# Yichin wants a secret number, for a thing.  I'll use whatever comes out of the
# fixed version of the Mangler when I put in something that breaks this version.
# Like, if the mangler currently breaks when I put in the number 7 -- it doesn't
# -- then the number I'm using to hide the thing is going to be whatever comes
# out of the fixed mangler when I put in 7.
# (Where "the fixed version" is just "the version with the broken line taken out")

# Third note from me: remember that the symbols in Python for the four main
# arithmetic operations are /+*-
# But probably not in that order.

# Step 3: output the mangled number
print("Your mangled number is:")
print(round(x))
