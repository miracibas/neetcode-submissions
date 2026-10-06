class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #SETUP
        
        #Creating a dict/hashmap
        count = {}
        #Creating the buckets
        freq = [[] for i in range(len(nums) + 1)] 

        #FILLING OUR LIST AND BUCKETS

        #Counting how many times a number n appears: key = n (the number itself) value = it's count (how many times it occurs in the list) incrementing the value by 1 everytime it appears 
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # For every number, count pair, add the count as the key to the bucket and add the number as a value
        for n, c in count.items():
            freq[c].append(n)
        
        #RETRIEVING K MOST FREQUENT ELEMENTS

        #Intializing an empty list for our results
        res = []
        #Loop through the buckets starting at the last index and stepping down
        for i in range(len(freq) -1, 0, -1):
        #For every number at the position i, append it to our result; This returns the numbers with the most occurences first because we start at the end and any empty key, value pairs will be skipped.
            for n in freq[i]:
                res.append(n)
        #We know that the length of our result will always be equal to K; because you cannot retrieve more frequent elements than there are in the list
                if len(res) == k:
                    return res
        

            


        