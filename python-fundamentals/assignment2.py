#------------------------ASSIGNMENT-2------------------------------

# Q1. Write a program that takes salary as input. Using conditional statements, 
# calculate the final tax rate based on these rules:
# If salary < 30,000→ 5%
# If salary is 30,000-70,000 → 15%
# If salary > 70,000 → 25%

# salary =int(input("Enter salary:"))
# if salary <30000:
#     print("tax rate is 5%")
# elif salary>=30000 and salary<=70000:
#     print("tax rate is 15%")
# else:
#     print("tax rate is 25%")



# Q2. Write a function that takes two integers a and b
#  and prints all even numbers between them (inclusive).

# def even_no(a,b):
#     for i in range(a,b+1):
#         if i%2==0:
#             print(i)
# even_no(1,20)



# Q3. Write a function that prints the digits of a number, n.
# For eg: n = 312, there are 3 digits in it 3, 1 and 2 & we need to print them.

# def digits(n):
#     while n>0:
#         print(n%10)
#         n=n//10
# digits(12034)



# Q4. Write a function to return the count the number of digits in a number, n.

# def count_digits(n):
#     count=0
#     while n>0:
#         count+=1
#         n=n//10
#     return count
# print(count_digits(5005))



# Q5. Write a function to return the sum of digits of a number, n.

# def sum_digits(n):
#     sum=0
#     while n>0:
#         i=n%10
#         sum = sum+i
#         n=n//10
#     return sum
# print(sum_digits(123))



# Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5

# i=1
# for i in range (1,101):
#     if (i%3==0 and i%5==0):
#         print(i)


# Q7. Design a program to continuously input a number n from user 
# & print if it is positive or negative until the user enters "Quit".
# def check_number():
#     while True:
#         n = input("enter any no. or ('quit' to stop)")
#         if n =="QUIT" or n=="quit":
#             break
#             print("GOODbye!")
        
#         n= int(n)
#         if n>0:
#             print("positive")
#         elif n<0:
#             print("negative")
#         else:
#             print("zero")
# check_number()



#Q8.Let's create a Simple Calculator that performs arithmetic operations. 
# Create a function calculator(a, b, operation) that performs 
# addition, subtraction, multiplication, or division based on the operation parameter.

# def calculator(a ,b, operation):
#     if operation=='+':
#         print("sum=" , a+b)
#     elif operation=='-':
#         print("subtraction=" , a-b)
#     elif operation=='*':
#         print("product=" , a*b)
#     elif operation=='/':
#         print("division=" , a/b)
#     else:
#         print("invalid operation")
# calculator(2,3,"+")
# calculator(2,3,"-")
# calculator(2,3,"*")
# calculator(2,3,"/")
# calculator(2,3,"=")



#Q9. Write a function is prime (n) 
# that returns True if n is a prime number and False otherwise, using a loop.

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range (2,n):
#         if n%i==0:
#             return False
#     return True
# print(is_prime(6))
# print(is_prime(19))



#Q10. Let's create a "Number Guessing Game". Given a secret number (already
# decided by you), write a program that asks the user to guess it and prints:
# "Too high" if the guess is above the number
# "Too low" if the guess is below
# if the guess matches  "Correct!"

def guess_no():
    secret_no=20
    while True:
        n=int(input("Enter ur guess:"))
        if secret_no == n:
            print("CORRECT!")
            break
        elif n<secret_no:
            print("Too low")
        else:
            print("Too high")
guess_no()
