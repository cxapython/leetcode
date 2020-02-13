from typing import List
# class Solution:
#     def removeDuplicates(self,nums:List[int]) -> int:
#         nums_length = len(nums)
#         count = 0
#         for index in range(nums_length):
#             if index+1<nums_length:
#                 new_index = index - count
#                 if nums[new_index]==nums[new_index+1]:
#                     print("nums",nums[new_index])
#                     del nums[new_index+1]
#                     count+=1
#         return len(nums),nums            

# public int removeDuplicates(int[] nums) {
#     if (nums.length == 0) return 0;
#     int i = 0;
#     for (int j = 1; j < nums.length; j++) {
#         if (nums[j] != nums[i]) {
#             i++;
#             nums[i] = nums[j];
#         }
#     }
#     return i + 1;
# }

class Solution:
    def removeDuplicates(self,nums:List[int]) -> int:
        """
        题目要求:空间复杂度O(1)
        因为题目要求返回的是不重复元素的个数，所以就不用考虑打印最终的元素。
        通过快慢指针的元素，对元素赋值，因为元素个数不变，所以在循环的时候以及使用索引的时候不受影响。
        i是为了统计不重复的元素的个数，nums[j]!=nums[i]为不重复的情况，然后i+=1是下一个元素的比较。
        nums[i]= nums[j]表示,把序号为j的元素作为下次开始比较的元素,因为上面执行了i+=1了。
        因为题目要求返回的是不重复元素的个数
        """
        if not nums:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i] = nums[j]

        #根据Python的语法可以改为下面的方式        
        # for _,v in enumerate(nums,1):
        #     if v!=nums[i]:
        #         i+=1
        #         nums[i] = v    
        return i+1        

if __name__ == "__main__":
    s = Solution()
    l:List[int] = [0,0,1,1,2,2,3,3,4,4,4]

    print(s.removeDuplicates(l))