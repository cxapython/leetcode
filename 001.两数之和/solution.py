from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d =dict()
        for index,item in enumerate(nums):
            if item in d:
                return [d[item],index]
            else:
                d[target-item] =  index 
                
            #或者   
            # if target-item in d:
            #     return [d[target-item],index]
            # d[item] = index

if __name__ == "__main__":
    l:list = [2,7,11,15,12]
    target:int = 19
    s = Solution()
    print(s.twoSum(l,target))            



            