class Solution:
    def isPalindrome(self, s: str) -> bool:

    #two pointers


    #right pointer 

        r = len(s)-1

    #left pointer 
        l = 0 

    #we need to check if everything is alphanumeric
    #ignore non alphanumeric
    #turn everything lowercase 

        while l < r:
        #this used to ignore everything that is not alphanumeric skip over it
            while l < r and not self.alphaNum(s[l]):
                l += 1

            while r > l and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False 

        

            l, r = l +1, r - 1

        return True

        #if it is alpha numeric we need to skip over it 
        #we are going to create our own alphNum funtiuon that we will call 

    def alphaNum(self,c): 

        return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))



    

        



        