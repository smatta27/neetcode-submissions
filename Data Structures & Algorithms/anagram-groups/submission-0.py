class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #groupding anagrams 
        # what data structure?? 
        # why time effecieny 

        #if a key does not exist creates an empty list a regular list cannot do that 
        res = defaultdict(list)


        #first loop through each word in strs

        for s in strs: 
            #create a count for each word 

            #create an count for each word 

            count = [0] * 26 
            #for each character in the word 
            for c in s: 
                #update count slot 
                #example if z at z add 1 
                count[ord(c)-ord('a')] += 1

            #change to tuple so immutable 
            #at count append the word s 

            #appending to the same key 
            #count is the key 
            res[tuple(count)].append(s)

        return list(res.values())

            

            

            


        