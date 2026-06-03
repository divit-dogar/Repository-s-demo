# Check for Anagrams
# Description: Determine if two strings are anagrams of each other.
# Input: "listen", "silent"
# Output: True

# by shortcut . 
'''
s1= input ("enter the first string:")
s2= input ("enter the second string:")

print (sorted(s1) == sorted(s2))

'''

s1= input ("enter the first string:")
s2= input ("enter the second string:")
if len(s1)!= len(s2):
    print ("false")
else:
    count={}

    for ch in s1:
        count [ch]=count.get(ch,0)+1
    
    for ch in s2:
        count[ch]= count.get(ch,0)-1

        is_anagram = True
        for value in count.values():
            if value !=0:
                is_anagram = False
                break
print (is_anagram)

