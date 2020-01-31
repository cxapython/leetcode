package main
import "fmt"

func solution(nums []int,target int) []int{
	m:=make(map[int]int)
	for index,value := range nums {
		if w,ok:=m[value];ok{
			return []int{w,index}
		} else{
			m[target-value] = index
		}
	}
	return nil
}
func main() {
	nums:=[]int{2,7,11,15,12}
	fmt.Println("nums",nums)
	target:=19
	fmt.Println(solution(nums,target))

}