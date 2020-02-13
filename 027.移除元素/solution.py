from typing import List
class Solution:
    def removeElement(self,nums:List[int],val:int)->int:
        i = 0
        for j,v in enumerate(nums):
            if v!=val:
                #i比j慢,如果不是目标之间就前移动。
                nums[i] =nums[j]
                i+=1


        # 数量少的时候下面方式更快
        # nums_length = len(nums)
        # while (i<nums_length):
        #     if nums[i]==val:
        #         nums[i] = nums[nums_length-1]
        #         nums_length-=1
        #     else:
        #         i+=1    

        return i    


if __name__ == "__main__":
      s = Solution()
      l = [1,2,3,0,3,3,5,1,3]
      target = 3
      print(s.removeElement(l,target))    