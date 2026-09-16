class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r = 0 , len(heights) - 1

        res = 0

        while l < r:
            #finding the waters height --> not the walls so use min

            #min of the heights times the width so r minus left
            area = min(heights[l], heights[r]) * (r-l)

            #compare the area with the area in result and update res based on that 
            res = max(res, area)


            #moving the smaller wall limits the total area
            # potentially find a taller wall thus larger area 
            if heights[l] <= heights[r]:

                l += 1

            else: 
                r -= 1

        return res 



            
        


        