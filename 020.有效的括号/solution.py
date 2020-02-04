"""
左括号的话就压栈，右括号如果匹配到之前左括号就出栈。
最后如果栈的长度为0,则表示匹配成功
"""

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dic= {")": "(", "}": "{", "]": "["}
        stack = []
        for item in s:
            if item in bracket_dic:
                value = stack.pop() if stack else ""
                if bracket_dic[item]!=value:
                    return False
            else:
                stack.append(item)    

        if not stack:
            return True
                        


if __name__ == "__main__":
    input_str = "(([]})"
    s = Solution()
    print(s.isValid(input_str))        
