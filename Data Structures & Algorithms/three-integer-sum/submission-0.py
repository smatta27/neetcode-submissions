class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = [] 
        nums.sort()

        for i, a in enumerate(nums):

            #since we alrd sorted and 
            #if we start w a being positive stop
            if a > 0: 
                break

            #skip duplicates 
            if i > 0 and a == nums[i -1]:
                continue 

            #since i is already the index of a we need left to not also be a
            #skipping repeating a
            l, r = i + 1, len(nums) - 1

            while l < r: 
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r-=1
                elif threeSum < 0: 
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])

                #to look for a new triplet move both of the pointers
                    l += 1
                    r -= 1

                    #skipping duplicates
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res




                


            


            

            






        
        