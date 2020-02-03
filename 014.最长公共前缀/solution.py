from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        if len(strs) == 0:
            return ""
        prefix = strs[0] #把第一个字符串当做前缀
        
        for i in range(len(strs)):
            while strs[i].find(prefix) != 0: #如果其他的字符串不包含
                prefix = prefix[:-1] #从后面开始减少一个看看
                if not prefix:
                    return ""    
        return prefix            



# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:     
#         s = ""
#         print("*strs is ",*strs)

#         for i in zip(*strs):
#             print("i",i)
#             if len(set(i)) == 1:
#                 s += i[0]
#             else:
#                 break           
#         return s  
if __name__ == "__main__":
    s= Solution()
    input = ["flower","flow","flight"]
    print(s.longestCommonPrefix(input))        