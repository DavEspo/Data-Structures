# The two strings that are going to be compared
s = "anagram"
t = "nagaram"
# The array of all 0s with the length of the alphabet
Compare = [0]*26
# Function to test if the 2 strings are anagrams
def Anagram(string1,string2):
    # Loop that places values on the array based off the characters
    for i in range(len(s)):
        # Case where the string is a single character
        if len(s) & len(t) == 1:
            if ord(s) == ord(t):
                return True
            else:
                return False
        # Adds 1 with the first string and subtracts 1 on the second string at the location of the letter in the array
        Compare[ord(s[i])-ord('a')] = Compare[ord(s[i])-ord('a')] + 1
        Compare[ord(t[i])-ord('a')] = Compare[ord(t[i])-ord('a')] - 1
    # Case where the string is empty or multiple characters
    # Will have all 0's only if both strings had the exact same characters used
    if Compare == [0]*26:
        return True
    else:
        return False
# Calls the function with the input of the 2 strings
print(Anagram(s,t))
