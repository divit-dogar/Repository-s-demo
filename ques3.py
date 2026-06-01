# calculate the num of vowels in a string .

a=input("Enter a string: ")
count=0

for x in a :
    if x in "aeiouAEIOU":
        count+=1
print("number of vowels in the string is: ",count)