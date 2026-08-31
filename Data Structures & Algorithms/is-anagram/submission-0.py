class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


#checking if len(s) and len t are equal if not they literally cannot be anagrams 
        if len(s) != len(t):
            return False

#creating a list with 26 slots each slot for the alphabet 

        count = [0] * 26

        for i in range(len(s)):

            #find this position in the count and add 1
            count[ord(s[i]) - ord('a')] += 1
            #find this position in the count and subtract one 
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:

            #ok now lets look inside of count and if it is not equal to zero as it should cancel out reuturn false else it is an anagram 
            if val != 0:
                return False

        return True
    



