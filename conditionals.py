# Eg WAP to show if you are eligible to vote or not

# age =int(input("Enter your age:"))
# if (age>=18):
#     print("you can vote")
# else: 
#     print("you can't vote")



# WAP to tell about traffic light colors

# color = input("Enter color:")
# if color =="green":
#     print("GO")
# elif color =="yellow":
#     print("LOOK")
# elif color =="red":
#     print("STOP")
# else:
#     print("wrong traffic light color")



# WAP to show if age is less than 13 print child , if btw 13 and 18 print teenager , 
# greater than 18 print adult

# age = int(input("Enter ur age:"))
# if (age<13):
#     print("Child")
# elif (age>=13 and age<18):
#     print("teenager")
# else:
#     print("Adult")



#WAP if username is not == admin priunt wrong username
#and if password is not equal to pass print wrong password

# username=input("Enter username:")
# password=input("Enter password")
# if (username!= "admin"):
#     print("wrong username")
# elif password!= "pass":
#     print("wrong password")
# else:
#     print("login successful")

#or

# username=input("Enter username:")
# password=input("Enter password")
# if (username=="admin" and password=="pass"):
#     print("login")
# elif (username!="admin"):
#     print("wrong username")
# else:
#     print("wrong password")



#WAP to check a number n is multiple of 5 or not

# n=int(input("Enter any no."))
# if(n%5==0):
#     print("multiple of 5")
# else:
#     print("not a multiple of 5")



#WAP to print if any number n is odd or even

# n = int(input("enter any no."))
# if (n%2==0):
#     print("EVEN")
# else:
#     print("ODD")



#nesting 
#WAP if username is not == admin priunt wrong username
#and if password is not equal to pass print wrong password

# username=input("enter username:")
# password=input("enter password:")
# if (username=="admin" and password=="pass"):
#     print("LOGIN")
# else:
#     if (username!="admin"):
#         print("wrong username")
#     else:
#         print("wrong pass")



#matchcase
# WAP to tell about traffic light colors

color =input("Enter any color:")

match color:
    case "green":
        print("GO")
    case "yellow":
        print("LOOK")
    case "red":
        print("STOP")
    case _ :
        print("Wrong traffic light color")