#Write a program for create unique reference number like below format
#AP1A0001 , its will be auto generated like AP1A0002 for next record, 
#if AP1A9999 then next reference number will be AP1B0001,
#  if AP1Z9999 then next number will be AP2A0001

def generate_ref_num(ref ):

    prefix = ref[:2]   # AP
    digit = int (ref[2]) #1
    char = ref[3] #A
    num = int (ref[4:]) #0001

    if num <9999:
        num +=1
    else:
        num = 1
        if char< "z":
            char= chr(ord(char)+1)
        else:
            char = "A"
            digit +=1

    return prefix + str(digit)+ char +str(num).zfill(4)
new_ref = generate_ref_num("AP1A0001")
print(new_ref)  # Output: AP1A0002    

    