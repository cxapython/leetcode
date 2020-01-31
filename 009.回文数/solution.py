class Solution:
    def __init__(self):
        pass
    def isPalindrome(self,num:int)->bool:
        # if str(num)==str(num)[::-1]:
        #     return True 

        flag = False
        if num<0 or (num%10==0 and num!=0):
            pass
        else:
            res = 0
            #x的位数不断弹出，压入res。num >res表示res的位数没超过num。
            while num > res:
                res = res * 10 + num % 10 
                num //= 10
            
        return num==res or num==res//10          


if __name__ == "__main__":
    s = Solution()
    for i in [123,321,1234321,242]:
       print(s.isPalindrome(i))




        



