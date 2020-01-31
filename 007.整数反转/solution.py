"""
python的负数取模会得到一个正数。
"/"  表示浮点数除法，返回浮点结果;
"//" 表示整数除法,返回不大于结果的一个最大的整数
"""

class Solution:
    def reverse(self, x: int) -> int:
        y, res = abs(x), 0
        #因为x的范围在[-2^31,2^31-1]，所以如果x为负数时，其绝对值对应的范围就是1 << 31
        of = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > of: return 0
            y //= 10
        return res if x > 0 else -res

if __name__ == "__main__":
    s = Solution()
    print(s.reverse(-231))
    # l =[1,0,123,320,-231,1534236469]
    # for item in l:
    #     print(s.reverse(item))        