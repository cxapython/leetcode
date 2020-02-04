package main
import (
	"fmt"
)

func isValid(s string) bool {
    bracket_dic:=map[byte]byte{')': '(', '}': '{', ']': '['}
    var stack []byte
    for _,value:= range s{
    	l_s:=len(stack)
    	if l_s>0 {
    	if v,ok:=bracket_dic[byte(value)];ok{
    		top_element:=stack[l_s-1]
    		if v==top_element{
    			 stack = stack[:l_s-1]
    			 continue
    		}
    	}
      }
    	stack=append(stack,byte(value))
    	
    
    }
    return len(stack)==0

}
                        
func main() {
	 
	 fmt.Println(isValid("({})"))
}