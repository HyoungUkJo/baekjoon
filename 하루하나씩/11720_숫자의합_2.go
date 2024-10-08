package main

import "fmt"


func main() {
	var N int
	var nums string
	sum := 0

	fmt.Scan(&N)
	fmt.Scan(&nums)

	for i:=0; i<len(nums); i++ {
		digit := int(nums[i] -'0')
		sum+=digit
	}
	fmt.Print(sum);
}
/* func main() {
	var N int
	var nums int
	var sum int = 0

	fmt.Scan(&N)
	fmt.Scan(&nums)

	for nums > 0 {
		sum += nums%10
		nums /=10
	}

	fmt.Print(sum)
} */