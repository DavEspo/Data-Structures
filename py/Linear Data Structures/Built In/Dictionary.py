# Import defaultdict
from collections import defaultdict

# Input list
strs = ["eat","tea","tan","ate","nat","bat"]

# Function that groups the anagrams together
def groupingAnagrams(Inputlist):
    # Sets up the count array of 26 0's
    count = [0] * 26
    # empty defaultdict creation
    d = defaultdict(list)
    # loop that counts the words
    for a in Inputlist:
        # # count of characters
        for b in a:
            # convert the character count
            count[ord(b)-97] = count[ord(b)-97] + 1
        # list to tuple
        t = tuple(count)
        # Use the tuple as key to Defdict
        d[t].append(a)
        # Reset count for next loop
        count = [0] * 26
    # Return the values of default
    return d.values()

# Calling the function to group the anagrams
print(groupingAnagrams(strs))
