# number to word

num = int (input("enter the number:"))

ones= ("", "one" ,"two", "three", "four", "five", "six","seven","eight","nine")
tens= (" ", " ","twenty", "thirty", "forty", "fifty", "sixty","seventy","eighty","ninety")
teens =("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen","seventeen","eighteen","nineteen")

if num ==0:
    print ("zero")
else:
    if num>=100:
        print(ones[num//100]+"hundred", end="")
        num = num%100
    if 10 <= num <= 19:
        print(teens[num-10],end="")
    else:
        if num>=20:
            print(tens[num//10],end="")
            num = num%10
        if num>0:
            print(ones[num], end="")
    