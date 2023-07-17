package main

import "fmt"

func removeDuplicates(nums []int) int {

	var index int
	length := len(nums)
	for i := 0; i < length-1; i++ {
		if nums[index] == nums[index+1] {
			nums = append(nums[:index+1], nums[index+2:]...)
		} else {
			index += 1
		}
	}
	return len(nums)
}

func main() {
	nums := []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
	fmt.Println(removeDuplicates(nums))
}
