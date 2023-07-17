package main

import "fmt"

func plusOne(digits []int) []int {

	for i := len(digits) - 1; i >= 0; i-- {
		sum := digits[i] + 1
		if sum != 10 {
			digits[i] = sum
			break
		} else if i == 0 {
			digits = append([]int{1, 0}, digits[1:]...)
			break
		} else {
			digits[i] = 0
		}
	}
	return digits
}

func main() {
	digits := []int{9, 9, 8}
	fmt.Println(plusOne(digits))
}
