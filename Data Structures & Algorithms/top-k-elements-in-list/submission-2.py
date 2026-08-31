class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #top k frequent elements 
        #bucket sort 
        #were going to create a bucket sort algorithm 
        #create a hashmap 
        count = {}
        #create frequency table 
        freq = [[] for i in range (len(nums) + 1)]

        #update the frequency of each word depending on how many times its appearing 

        for num in nums: 
            #at each num update the count 
            #at the key if alrd in dictionary update; add one to count 
            #if not then update to 1 
            count[num] = 1 + count.get(num, 0)
        #for the number and count in the dictionary
        for num, cnt in count.items():
            #update teh frequency 
            freq[cnt].append(num)

            #final list to return 

            res = [] 

            #we want most occuring so go from higher index, stop at 0 and subtract by 1
        for i in range(len(freq) - 1, 0, -1):
                #get the number 
                #for the number in the index append it to the result 
            for num in freq[i]:
                res.append(num)
                    #but if we alrd reached the k most stop and return what we have 
                if len(res) == k: 
                    return res 









        

        













        

            











