class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""  # Start with an empty result string
        for s in strs:  # Go through each string in the list
            res += str(len(s)) + "#" + s  # Add "length of string" + "#" + "string" to the result
        return res


    def decode(self, s: str) -> List[str]:
        res = []  # Start with an empty list to hold the decoded strings
        i = 0  # Start reading from the first character of the string
        
        while i < len(s):  # Keep going until you've read the whole string
            j = i  # Set `j` to the same position as `i`
            
            # Find the "#" to know where the length part ends
            while s[j] != "#":
                j += 1
            
            # The number between `i` and `j` is the length of the string
            length = int(s[i:j])
            
            # Add the substring that starts after "#" and is `length` characters long
            res.append(s[j + 1:j + 1 + length])
            
            # Move `i` to the start of the next encoded string
            i = j + 1 + length
        
        return res
