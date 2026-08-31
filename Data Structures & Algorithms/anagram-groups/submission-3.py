class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #grouping words that are anagrams 
        #dictionary/hashmap 

        #create a defaultdict cause we alrd have a list 
        #this will automatically create n spots for each item within the list 


        res = defaultdict(list)

        #once we create a default dictionary lets go through each item 
        #update each slot in the dic with 26 available keys s

        for s in strs: 
            
            #creating a list count with 26 slots of zeros for each string
            count = [0] * 26

            #create another for loop for 
            for c in s:
                count[ord(c)- ord('a')] += 1

            #lists cannot be keys because therye mutable convert into a tuple 

            res[tuple(count)].append(s)

        #finally return the enture updated ;ist 
        #only return the anagrams 
        return list(res.values())



         
    




            

            

        

            

            

            


        