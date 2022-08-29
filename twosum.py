class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for i,e in enumerate(nums):
                
             if  e not in dic.keys():   
                    dic[target-e]=i
             else:
                return [int(dic[e]),i]

        return []    
        

            