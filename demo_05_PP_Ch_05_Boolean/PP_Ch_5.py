# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business 
# University of Central Florida
#
# January 7, 2021
# 
##################################################
#
# Demo for Chapter 5: Making Choices (Boolean Variables)
#
##################################################
"""


##################################################
## A Boolean Type
##################################################

# Named after George Boole (1815-1864), a boolean variable, 
# of type bool takes on one of two values: 
# True or False.

#-------------------------------------------------
### Boolean Operators
#-------------------------------------------------

# The negation not is a unary operator on type bool

not True

not False

# It negates, or reverses, the Boolean variable, 
# from False to True or vice versa. 

# The binary operator and returns True only if both
# operands are True.

 
True and True

False and False

True and False

False and True

 
# The binary operator or returns True if either
# one of the operands are True.

 
True or True

False or False

True or False

False or True


# As with any other value, you can store these as variables. 
 
cold = True
windy = False
(not cold) and windy

not (cold and windy)



#-------------------------------------------------
#### Building an Exclusive or Expression
#-------------------------------------------------

# The *exclusive or* operand returns True if only one
# of the operands is True. 

# If you want an exclusive or, you can construct it from 
# multiple Boolean operators. 

 
b1 = False
b2 = False
(b1 and not b2) or (b2 and not b1)

b1 = False
b2 = True
(b1 and not b2) or (b2 and not b1)

b1 = True
b2 = False
(b1 and not b2) or (b2 and not b1)

b1 = True
b2 = True
(b1 and not b2) or (b2 and not b1)


# We will see an easier way to do this after introducing more operators.


#-------------------------------------------------
### Relational Operators
#-------------------------------------------------

# Relational operators compare operands to produce a Boolean variable.
# Inequality signs are a primary example.

45 > 34

45 > 79

45 < 79

45 < 34

 
# The default is strict inequality but the "equal"" case
# is specified by adding an equal sign. 
 
23.1 >= 23

23.1 >= 23.1

23.1 <= 23.1

23.1 <= 23


# A double equal sign == denotes a test for equality
# of the opearands and returns True if they are equal. 
 
67.3 == 87

67.3 == 67

67.0 == 67


# The exclamation mark ! denotes negation, 
# so the combined operator != tests for inequality, 
# returning True only if the operands are not equal. 

67.0 != 67

67.0 != 23


# The examples above show how the operators work but 
# these operators are more interesting and useful when 
# the operands are variables, as in the is_positive function, 
# which is another way to evaluate Boolean variables. 
 
def is_positive(x: float) -> bool:
    """Return True iff x is positive.

    is_positive(3)
    True
    is_positive(-4.6)
    False
    """
    return x > 0

is_positive(3)

is_positive(-4.6)

is_positive(0)


# Now we can revisit the example with exclusive or operator, 
# applied to two variables of type bool. 

b1 != b2

# This expression returns True only if exactly one of them is True. 
# Consider all the possible combinations of True and False for each variable, if you need to convince yourself.

b1 = False
b2 = True
b1 != b2

b1 = True
b2 = True
b1 != b2


#-------------------------------------------------
### Combining Comparisons
#-------------------------------------------------

# You can pass other expressions as the operands in relational operators. 
# Just as with numbers, there is an order of operations with type bool.

# 1. Arithmetic operators are evaluated first: 
# you have to know the values you are comparing first. 
# 1. Relational operators all have the same precedence, after arithmetic operators. 1. Boolean opearators like and, or and not are evaluated last: again, you have to know the values you are comparing first. 

# Once you know these rules, you can avoid typing parentheses. 

x = 2
y = 5
z = 7
x < y and y < z
 
# This returns the same:

x = 5
y = 10
z = 20
(x < y) and (y < z)
 

# These examples determine whether a number lies within an interval. 
 
x = 3
(1 < x) and (x <= 5)

x = 7
(1 < x) and (x <= 5)


# You can also write it the way it would be written on paper, 
# by *chaining* the comparisons. 

x = 3
1 < x <= 5
 
# Most cases work as you expect but sometimes there are surprises:
 
3 < 5 != True

3 < 5 != False


# Recall the order of operations: the relational operator
# is evaluated first and 5 is neither True nor False. 


#-------------------------------------------------
#### Using Numbers and Strings with Boolean Operators
#-------------------------------------------------

# A zero is False and all other numbers return True.
 
not 0

not 1

not 34.2

not -87

 
# Similarly for strings, the empty string'' returns False
# and all other strings return True. 
 
not ''

not 'bad'



#-------------------------------------------------
### Short Circuit Evaluation
#-------------------------------------------------

# When evaluating a Boolean expression, once Python
# has enough information to know that a condition is 
# True or False, it stops evaluating. 
# This is called *short circuit evaluation*. 

# For example, in an or expression, once one operand is True, 
# the full expression returns True.

# We can illustrate this with an opearand that throws an error. 

1 / 0
 
# Now try this in an *or* expression: 
 
(2 < 3) or (1 / 0)


# What happened? Python didn't bother evaluating the second operator, 
# avoiding the error. 


#-------------------------------------------------
### Comparing Strings
#-------------------------------------------------

# Python compares strings by the corresponding binary values in an
# ASCII table. 
# In this ordering, the capital letters come first. 

'A' < 'a'

'A' > 'z'


# If a shorter string runs out of letters, it is less than the other. 
 
'abc' < 'abd'

'abc' < 'abcd'
 

# The in operator checks whether a string is contained within another string. 
 
'Jan' in '01 Jan 1838'

'Feb' in '01 Jan 1838'

date = input('Enter a date in the format DD MTH YYYY: ')
# Enter a date in the format DD MTH YYYY: 24 Feb 2013
'Jan' in date

date = input('Enter a date in the format DD MTH YYYY: ')
# Enter a date in the format DD MTH YYYY: 03 Jan 2002
'Jan' in date

'a' in 'abc'

'A' in 'abc'

'' in 'abc'

'' in ''



##################################################
## Choosing Which Statements to Execute
##################################################

# The primary purpose of Boolean variables is for the Python to
# follow different instructions under different conditions.
# An if statement evaluates conditions in a code block 
# if the condition is True. 

ph = float(input('Enter the pH level: '))
# Enter the pH level: 6.0
if ph < 7.0: 
    print(ph, "is acidic.")

 

# If the condition is not true, nothing happens.
 
ph = float(input('Enter the pH level: '))
# Enter the pH level: 8.0
if ph < 7.0:
    print(ph, "is acidic.")


# Just as with the def keyword, the block of statements
# must be indented.

 
ph = float(input('Enter the pH level: '))
# Enter the pH level: 6
if ph < 7.0:
print(ph, "is acidic.")


# If the condition is True, the entire block will
# be executed. 
 
ph = float(input('Enter the pH level: '))
# Enter the pH level: 6.0
if ph < 7.0:
    print(ph, "is acidic.")
    print("You should be careful with that!")
 

# Any statements that are not indented after the block 
# will be executed regardless of the condition for the 
# indented block. 
 
ph = float(input('Enter the pH level: '))
# Enter the pH level: 8.0
if ph < 7.0:
    print(ph, "is acidic.")

print("You should be careful with that!")


# The commands following the block of commands in the if statements
# must be separated by a blank line to signal the end of the if statement: 
 
ph = float(input('Enter the pH level: '))
# Enter the pH level: 8.0
if ph < 7.0:
    print(ph, "is acidic.")
print("You should be careful with that!")

# However, this is not true for all versions of Python.
# It is simply good form to leave a blank line to separate 
# blocks of code. 


# This is not a problem when the if condition is False. 

ph = 8.0
if ph < 7.0:
    print(ph, "is acidic.")
print("You should be careful with that!")


# Another if statement can follow right after
# the previous one, regardless of the outcome of the first. 

ph = float(input('Enter the pH level: '))
# Enter the pH level: 8.5
if ph < 7.0:
    print(ph, "is acidic.")

if ph > 7.0:
    print(ph, "is basic.")


# We can merge these cases by following the block with an elif, 
# which stands for "else if". 
 
ph = float(input('Enter the pH level: '))
# Enter the pH level: 8.5
if ph < 7.0:
    print(ph, "is acidic.")
elif ph > 7.0:
    print(ph, "is basic.")
 

# Notice that the sequence of if and elif statements
# may not cover all possibilities. 

 
ph = float(input('Enter the pH level: '))
# Enter the pH level: 7.0
if ph < 7.0:
    print(ph, "is acidic.")
elif ph > 7.0:
    print(ph, "is basic.")



# The elif statement accomplished the same thing as the 
# if statement. 
# This is not always the case, particularly if the first block
# changes the value of the variables. 

 
ph = float(input('Enter the pH level: '))
# Enter the pH level: 6.0
if ph < 7.0:
    ph = 8.0

if ph > 7.0:
    print(ph, "is acidic.")


# The first block changed the value of the ph variable, 
# changing the outcome in the second block. 
# This is not the case when the blocks are connected with an elif statement. 

ph = float(input('Enter the pH level: '))
# Enter the pH level: 6.0
if ph < 7.0:
    ph = 8.0
elif ph > 7.0:
    print(ph, "is acidic.")

    

# In this case, the elif block is skipped. 


# You can chain multiple elif statements to test a sequence of conditions. 

compound = input('Enter the compound: ')
# Enter the compound: CH4
if compound == "H2O":
    print("Water")
elif compound == "NH3":
    print("Ammonia")
elif compound == "CH4":
    print("Methane")




# If none of the conditions are satisfied, nothing is executed, 
# which may not be what you want. 
# The else statement is executed in this case. 

 
compound = input('Enter the compound: ')
# Enter the compound: H2SO4
if compound == "H2O":
    print("Water")
elif compound == "NH3":
    print("Ammonia")
elif compound == "CH4":
    print("Methane")
else:
    print("Unknown compound")




##################################################
## Nested if Statements
##################################################

# An if statement block can contain any kind of Python
# statement, including another if statement. 
# The inner if statement is called a *nested if statement*. 

value = input('Enter the pH level: ')
if len(value) > 0:
    ph = float(value)
    if ph < 7.0:
        print(ph, "is acidic.")
    elif ph > 7.0:
        print(ph, "is basic.")
    else:
        print(ph, "is neutral.")
else:
    print("No pH value was given!")

 



##################################################
## Exercises
##################################################


### Exercise 9
 
ph = 2
if ph < 7.0:
    print(ph, "is acidic.")
elif ph < 3.0:
    print(ph, "is VERY acidic! Be careful.")



# What happens when ph = 6.4?

# What happens when ph = 3.6?

# Is this the intended result? If not, how could you fix it? 



### Exercise 10
 
ph = float(input("Enter the ph level: "))
if ph < 7.0:
    print("It's acidic!")
elif ph < 4.0:
    print("It's a strong acid!")
 

# What happens when ph = 6.4?

# What happens when ph = 3.6?

# Is this the intended result? If not, how could you fix it? 
# Consider a different approach from the example above. 

# What change would you make to print both messages when they are true?



##################################################
## End
##################################################
