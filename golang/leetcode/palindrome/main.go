package main

import "fmt"

func isPalindrome(x int) bool {
	var result int = 0

	num := x
	for x > 0 {
		result = result*10 + x%10
		x = x / 10
	}

	return result == num
}

func main() {
	num := 101

	fmt.Println(isPalindrome(num))
}
