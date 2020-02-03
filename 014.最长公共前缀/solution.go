package main
import(
"fmt"
 "strings"
)

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	prefix := strs[0]
	for _,value:=range strs {
		for strings.Index(value,prefix)!=0{
			prefix = prefix[0:len(prefix)-1]
			if prefix==""{
				return ""
			}

		}

	}
	fmt.Println(prefix)
	return prefix

    
}

func main(){
	l:=[]string{"flower","flow","flight"}
	longestCommonPrefix(l)
}


// class Solution:
//     def longestCommonPrefix(self, strs: List[str]) -> str: 
//         if len(strs) == 0:
//             return ""
//         prefix = strs[0] #把第一个字符串当做前缀
        
//         for i in range(len(strs)):
//             while strs[i].find(prefix) != 0: #如果其他的字符串不包含
//                 prefix = prefix[:-1] #从后面开始减少一个看看
//                 if not prefix:
//                     return ""    
//         return prefix   