#DO NOT TOUCH
from os import system
system('cls')
#DO NOT TOUCH

#Input and strings.
#Let you recieve a string from the user 
yourName = input("Tell me your name: ")     #Display the output "Tell me your name" #Saves the string inside yourName Variable


#Input and Numbers.
#Let you recieve a number
yourAge = int(input("Tell me your age: "))    #Display the output "Tell me your number" #Saves the number inside yourAge Variable.

#int method returns an integer object from the given number or string

stringNumber = input("Tell me a  string number: ")   #Output:Output the number that you give as an string value 


#Format 
#String interpolation.  #Process of inseting a custom string or variable in predefined text. 
matiasName = "Matias"
matiasAge = 23

print("Hello my name is {} . I'm {} years old".format(matiasName, matiasAge))
print(f"Hello my name is {matiasName} . I'm {matiasAge} years old")

print(stringNumber)
print(type(stringNumber))