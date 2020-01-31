package main
import "fmt"
func isPalindrome(num int) bool {
    flag:=false
    if (num<0) || (num%10==0&&num!=0){

    }else{
        res := 0
        for num > res {
            res = res * 10 + num%10
            num /= 10
        }
        flag = num==res || num==res/10
    }
    return flag
    
}
func main() {
    l:=92329
    fmt.Println(isPalindrome(l))

}