class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #return the indices that add up to to the target of the list 

        prevMap = {} 

        for i, n in enumerate(nums):

            diff = target - n

            if diff in prevMap: 
                return [prevMap[diff], i]

            #think like else statement updates the prevmap 

            prevMap[n] = i 


        
        

        