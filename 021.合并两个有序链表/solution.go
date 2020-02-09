package main
import "fmt"
type ListNode struct {
      Val int
      Next *ListNode
} 
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	var head *ListNode
	var pre *ListNode
	head = &ListNode{Val:-1}
	pre = head
	for l1!=nil && l2!=nil {
		if l1.Val <= l2.Val{
			head.Next = l1
			l1 = l1.Next
		}else{
			head.Next = l2
			l2 = l2.Next
		}
		head = head.Next
	}
	if l1!=nil{
		head.Next = l1

	}
	if l2!=nil{
		head.Next = l2
	}
	return pre.Next
}

func reverse(l *ListNode){
	cursor:=l
	for cursor!=nil {
		fmt.Println(cursor.Val)
		cursor= cursor.Next
	}
}
func main(){
	l1:=&ListNode{Val:1}
	l1.Next = &ListNode{Val:2}
	l1.Next.Next = &ListNode{Val:9}

	l2:=&ListNode{Val:3}
	l2.Next = &ListNode{Val:4}
	l2.Next.Next = &ListNode{Val:8}
	l2.Next.Next.Next = &ListNode{Val:10}
    new_l:=mergeTwoLists(l1,l2)
    reverse(new_l)




}