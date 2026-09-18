class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mp = {}

        l = 0 
        res = 0

        #for index use in range
        #sliding window problem 
        for r in range(len(s)):
            #if its alrd in the map 
            #move our left pointer 
            if s[r] in mp:
                #if the right ndex is alrd in the map 
                #were going to move l, cannot move l backwards 
                l = max(mp[s[r]] + 1, l)

            
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res



       


        