# reverse a num using recursion

def reverse_num(num, rev=0):
    if num==0:
        return rev
    else:
        rev=rev*10 +num%10
        return reverse_num(num//10, rev)
print(reverse_num(12345))  