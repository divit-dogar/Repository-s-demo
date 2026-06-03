# reverse a string without using built in function

s=input("Enter a string: ")
revers =""

for x in s:
    revers = x + revers 
print("reverse of the string is: ",revers)

