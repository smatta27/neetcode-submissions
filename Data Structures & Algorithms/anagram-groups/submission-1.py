class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #group anagrams 
        #how do we check this create a dictionary and we have to group together anagrams 

        #create a dictionary 

       #create a dictionary 
        groups = {}

        #for every single work in the list 
        for word in strs:
            #we are going to add this sorted word to key 
            key = "".join(sorted(word))

            #check our dictionary if it is a new key thats not already in the dictionary create a new key 
            if key not in groups:
                groups[key] = []

            #now in groups at the correct key we are going to append the word 
            groups[key].append(word)
            
            
        #output only the values in the dictionary 
        return list(groups.values())

            

        

            

            

            


        