class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def merge_two_list(self,l1:ListNode,l2:ListNode)->ListNode:
        #pre是哨兵节点，head是每次要移动的
        pre=head = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                #head的next指向l1
                head.next = l1
                #l1前移
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next  
            #指向比较完之后数据，进行下一轮比较    
            head = head.next
        #剩下的部分是没有比较的             
        head.next = l1 if l1 is not None else l2
       
        return pre.next

def traverse_list(l):
    cursor = l
    while cursor is not None:
        print(cursor.val)
        cursor = cursor.next
            

if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(20)    
    l.next.next = ListNode(200) 
    l.next.next.next = ListNode(2001)

    l2 = ListNode(2)
    l2.next = ListNode(21)
    s = Solution() 
    new_l=s.merge_two_list(l,l2)    
    traverse_list(new_l)              




        