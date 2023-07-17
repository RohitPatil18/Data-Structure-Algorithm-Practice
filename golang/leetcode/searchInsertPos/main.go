package main

import "fmt"

func searchInsert(nums []int, target int) int {
	for idx, num := range nums {
		if num == target || num > target {
			return idx
		}
	}
	return len(nums)
}

func main() {
	var nums []int = []int{1, 3, 5, 6}
	var target int = 7

	fmt.Println(searchInsert(nums, target))
}
