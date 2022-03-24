#DO NOT TOUCH
from os import system
system('cls')
#DO NOT TOUCH

#Conditional statements in Python. 
#Decision making is fundamental when programming.
#Conditional statements evaluates the code to see if meets the specified conditions. 

#Python has six conditional statements that are used in decision-making

#1.-If the statement

# if expression 
#     Statement

#if condition is true, the statement will be executed.
num = -5 
if num < 0:
    print(f"{num} is a negative number.")   #Output: num is a negative number.
print("This statement is True.")    #Output: This statement is True.


#2.-If Else Statement

# if condition :
    #Will execute this block if the condition is True.
# else:
    #Will execute this block if the condition is True.

#Using the same of num = -5
if num >= 0:
    print(f"{num} is equal or greater than zero!")
else:
    print(f"{num} is a number less than zero!")


#3.- The if/elif/else Statement. 

#if condition:
    #body of if

#elif condition:
    #body of elif

#else condition:
    #body of else

#Example 
#This code evaluates if the number is positive,negative or zero. 

num_1 = int(input("Give me a number! "))

if num_1 > 0:
    print(f"{num_1} is a positive number!")

elif num_1 == 0:
    print(f"You entered number {num_1}!")

else :
    print(f"{num_1} is a negative number!")













#4.-
#5.-
#6.-


