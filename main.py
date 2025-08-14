
#Python full name to UPPERCASE program 

#Ask the user to enter their first name 
#First_name = input("Please enter your first name: \n")

# Ask the user to enter their second name
#Last_name = input("Please enter your last name: \n")

#Print user's full name in UPPERCASE 
#full_name = f"{First_name} {Last_name}"

#print(f"Your full name is: {full_name.upper()}")


#Logical operators 

#age = input("How old are you?\n")
#if 18 <= int(age) <=45:
#if int(age) >= 18 and int(age) <= 45: # And helps to find the age range 
 #   print("You can have access.")
#else: 
 #   print("You are not allowed here.")

# Python Even or Odd program

# Ask user to input an integer 
#Question = input("input an integer \n")
# Find the integer moudulo 2 
#if int(Question) % 2 == 0: 
## if the modulo is equal to 2 print Even 
  #  print ("Even")
# Else print Odd 
#else:
 #   print("Odd")
    
# Python Grade Calculator program

# # Ask user to input thier score as a number 
# score = input("input your score: ")
# # If score is between 90 to 100 (inclusive) print grade A 
# if int(score) >= 90 and int(score)<= 100:
#     print("Grade A")
# # If score is between 80 to 89 (inclusive) print grade B
# if int(score) >= 80 and int(score)<= 89:
#     print("Grade B")
# # If score is between 70 to 79 (inclusive) print grade C 
# if int(score) >= 70 and int(score)<= 79:
#     print("Grade C")
# # If score is between 60 to 69 (inclusive) print grade D
# if int(score) >= 60 and int(score)<= 69:
#     print("Grade D")
# # If score is between 0 to 59 (inclusive) print grade F
# if int(score) >= 0 and int(score)<= 59:
#     print("Grade F")


# Ask user to input their score as a number
#score = float(input("Input your score: "))

# Check if the score is between 90 to 100 (inclusive)
#if 90 <= score <= 100:
 #   print("Grade A")
#else:
 #   print("Not Grade A")


# Ask user to input thier purchase amount as float 
purchase_amount =  float

# if the purchase is 1 cedis or more apply 2 % discount and print amount to pay 
# if the purhase is 5 cedis or more apply 1% discount and print amount to pay 
# if the purchase is less than 5 cedis apply no sicount and print amonunt to pay


# # Ask user to input the length of the 3 sides of a triangle
# x = float (input("Enter the first side"))
# y = float (input("Enter the second side"))
# z = float (input("Enter the third side"))
# # If all sides are equal print Equilateral
# if x == y and y == z:
#     print(f"you have an Equilateral")
# # If 2 sides are equz al print Isosceles
# elif x == y and y == z or x == z:
#     print(f"you have an Isosceles")


# List 
# file = open ("task.txt","r")
# print(file.read())

# file = open ("tasks.txt","r")
# tasks = file.read().split("\n")
# for task in tasks:
#     print(f"{tasks.index(task)+1}. {task}")

# Using loop 
# use loop to calculate the sum of the numbers below 
numbers = [10, 5, 20, 8, 15]

numbers = [10, 5, 20, 8, 15]
sum = 0
# total_sum = 0

# for number in numbers:
#     total_sum += number

# print("Sum of the numbers:", total_sum)

# for number in numbers:
#     sum = sum + number 
# print(sum)

# Open the file emails.txt in READ mode 
# Read and split the dat using \n to get a list 
# Lopp over the list emails and print a generated username for each of them
# i.e. username is all characters before the @ 


# Python function
#Define a register user function 

# # def calaculate_sum(num1, num2): 
# def register_user(name, email, password):
#   # Check if user does not already exist 
#   # Hash user password 
#   # Check if email is valid 
#   # Check if user is not a robot 
#   # Return response
#   return "User register successfully!"
# response = register_user("Nathan Lartey","nathanlartey33@gmail.com","123456")

import add
import show
import update
import delete

add_task_response = add.add_tasks("sleep")
print(add_task_response)

show_task_response = show.show_tasks()
print(show_task_response)

update_task_response = update.update_tasks("sleep", "Wake Up")
print (update_task_response)

delete_tasK_response = delete.delete_task("Wake Up")
print (delete_tasK_response)






