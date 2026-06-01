#Write a program to validate mobile number using regex
# without using regex.

num =input("Enter a mobile number: ")
if len(num)==10 and num[0] in "6789" and num.isdigit():
    print("valid mobile number")

else:
    print("invalid mobile number")


# with using regex

import re 
num =input("Enter a mobile number: ")

if re.fullmatch("[6-9][0-9]{9}",num):
    print("valid mobile number")
else:
    print("invalid mobile number")

 