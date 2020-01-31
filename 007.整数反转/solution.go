package main
import "fmt"
func reverse(x int) int {
        res:=0
        for x!=0{
        	res =res*10+x%10
        	if ((-1<<31) >= x || x>=(1<<31-1)) {
        		return 0

        	}
        	x/=10
        }
        return res
}

func main() {
	x:=[]int{1,123,0,321,-1241441}
	for _,v:=range x{
		fmt.Println(reverse(v))
	}
	
}