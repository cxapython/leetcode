package main
import "fmt"
func romanToInt(s string) int {
    dic:=map[string]int {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    sum:=0
    pre_num:=dic[string(s[0])]
    for i:=1;i<len(s);i++{
        value:=string(s[i])
        fmt.Println("value",value)
        num:=dic[value]
        if pre_num <num{
            sum-=pre_num
        }else{
            sum+=pre_num
        }
        pre_num = num

        }
         sum+=pre_num
        return sum    
    }  
       

func main() {
    fmt.Println(romanToInt("MCMXCIV"))
}

// class Solution:
//     def romanToInt(self, s: str) -> int:
//         dic ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
//         sum = 0
//         l=len(s)
//         pre_num = dic.get(s[0])
//         for index in range(1,l):
//             value=s[index]
//             num = dic.get(value)
//             if pre_num<num:
//                 sum -=pre_num
//             else:
//                 sum+=pre_num
//             pre_num = num
//         sum+=pre_num
//         return sum    
// 