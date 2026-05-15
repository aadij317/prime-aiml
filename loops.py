#infinite loop

# while True:
#     print("Hello World") #to exit press ctrl+c



#print hello world 5 times

# i=0
# while (i<5):
#     print("hello world")
#     i+=1



#print no. 1 to 5

# i=1
# while i<=5:
#     print(i)
#     i+=1



#reverse 5 to 1

# i=5
# while i>=1:
#     print(i)
#     i-=1



#multiplication table of n

# n= int(input("Enter any no:"))
# i=1
# while i<=10:
#     print(n*i) 
#     i+=1



#break
#WAP to print 1 to 10 and break the loop at 6

# i=1
# while i<=10:
#     if i==6:
#         break
#     print(i)
#     i+=1
# print("outside the loop now....")



#continue
#WAP to print no from 1 to 10 and skip multiples of 3

# i=1 
# while (i<=10):
#     i+=1
#     if (i%3==0):
#         continue
#     print(i)



#print all the odd no from 1 to 10

# i=1
# while (i<=10):
#     if (i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1




    ##for loops
#WAP to count no of i's in "artificial intelligence"

# word="artificial intelligence"
# count=0
# for i in word:
#     if i=='i':
#         count+=1
# print(count)



#WAP to print vowel count of a given string

# string="Aadi is such a cutiee!"
# count=0
# for i in string:
#     if (i in "aeiouAEIOU"):        #if (i=='aA' or i=='eE' or i=='iI' or i=='Oo' or i=='Uu'):
#         count+=1
# print("vowel count=", count)


#range function
#print sum of frist n natural no.s

# n=int(input("Enter any no"))
# sum=0
# for i in range(1,n+1):
#     sum+=0       #mathematical form (n*(n+1)/2)
# print("sum=", sum)



#function 

# def hello():
#     print("hello")
# hello()



#WA function sum(a,b) to return sum of a,b

# def sum(a,b):
#     s = a+b
#     return s
# print(sum(3,4))


#WAF to that input 3 values and return their average

# def avg(a,b,c):
#     average=(a+b+c)/3
#     return average
# print(avg(1,2,3))



#lambda function

# s= lambda a,b: a+b
# print(s(4,5))



#WAP to print factorial of 'n'
def calc_factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial
print(calc_factorial(5))