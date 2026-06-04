# find permutaion of string

def permutation(s, current=""):
    if len (s)==0:
        print (current)
    else:
        for i in range(len(s)):
            ch=s[i]
            left_sub_string= s[:i]
            right_sub_string= s[i+1:]
            remaining= left_sub_string + right_sub_string
            permutation(remaining , current +ch)

permutation("abc")
permutation("dogar")