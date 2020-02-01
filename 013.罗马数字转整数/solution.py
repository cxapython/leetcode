class Solution:
    def romanToInt(self, s: str) -> int:
        dic ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        l=len(s)
        pre_num = dic.get(s[0])
        for index in range(1,l):
            value=s[index]
            num = dic.get(value)
            if pre_num<num:
                sum -=pre_num
            else:
                sum+=pre_num
            pre_num = num
        sum+=pre_num
        return sum    
                        
            
            


        # special = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        # res = 0
        # for k,v in special.items():
        #     if k in s:
        #         s = s.replace(k,str(v))   
        #         res = res+v    
                
        # if len(s)>1:        
        #     count=0
        #     for item in s:
        #         v = dic.get(item,0) 
        #         if v<10:
        #             count=count+v
        #         else:
        #             res = res + v 
        #     res =res +count  
        # else:
        #     try:
        #        res= int(s)   
        #     except:
        #         res = dic.get(s)          
        # return res                               
 
if __name__ == "__main__":
    s = Solution()
    for item in ["D","MCMXCIV"]:
        print(s.romanToInt(item))       