class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

   

        #window size - most common letters 

        #lets say we have 5 a's and 2 bs
        #the window size is 7 and hte most frequent characters are 5 
        #so 7 - 5 = 2 , we can repalce 2 characters 
        #build a hashmap for key value pairs 

        count = {} 
        res = 0
        l = 0

        #to keep track of most common letter
        maxf = 0 

        for r in range (len(s)):
            #update count 
            #if that char alrd there update its count if not add 0 to it plus 1
            count[s[r]] = 1 + count.get(s[r], 0)
            #check the most common letter update maxF
            maxf = max(maxf, count[s[r]])

            #remember k is the number we can replace 

            #the sliding window is represented by r - l + 1
            while (r - l + 1) - maxf > k: 

                #its invalid if its greater than k make our window smaller 
                #remove one count from our window
                count[s[l]] -= 1
                #update l's position 
                l += 1
            #longest valid substring 
            res = max(res, r - l + 1)
        return res 


















        