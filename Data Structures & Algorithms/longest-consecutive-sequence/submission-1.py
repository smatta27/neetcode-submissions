class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        #go through nums creating set to make sure it doenst have duplicates
        numSet = set(nums)

        #keep track of longest cons seq
        longest = 0

        #iterate through nums: 
        for n in nums: 
            #check if start of sequence but how? 
            #in order to check check if it has a left neighbor

            if(n -1) not in numSet: 
                #if it doesnt have a left neighbor its a start of a sequence 
                length = 0 

                #understand this 
                while(n + length) in numSet: 
                    length +=1 
                longest = max(length,longest)

        return longest
                





        