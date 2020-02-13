package main
import "fmt"

func removeElement(nums []int,val int) int {
	
	//双指针快慢指针
	// i:=0
	// for j,v:=range nums{
	// 	if nums[j]!=val {
	// 		nums[i] = nums[j]
	// 		i++
	// 	}
	// }
	// return i
    
    //数量少的时候下面方式更快 
    i:=0
	nums_length := len(nums)
    for i<nums_length{
    	if nums[i]==val {
    		nums[i] = nums[nums_length-1]
    		nums_length--
    	}else{
    		i++
    	}

    }
    return i


}

func main() {
   l:=[]int{1,2,3,0,3,3,5,1,3}
   target :=3
   fmt.Println(removeElement(l,target))
}