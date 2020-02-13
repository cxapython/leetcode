package main 
import "fmt"
func removeDuplicates(nums []int) int {
    i:=0
    for j:=1; j<len(nums); j++ {
    	v := nums[j]
    	fmt.Printf("%v :v%v\n",nums[i],v)
    	if nums[i]!=v {
    		i++
    		nums[i] = v
    	}
    }
    return i+1

}

func main() {
	l:=[]int{1,2,3,4,5,5}
	fmt.Println(removeDuplicates(l))

}