package main

import "fmt"

func twoSum(nums []int, target int) []int {

	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return []int{0, 0}
}

func main() {
	nums := []int{2, 11, 11, 7}
	target := 9

	results := twoSum(nums, target)

	if results[0] == 0 && results[1] == 0 {
		fmt.Println("Results not available.")
		return
	}

	fmt.Println(results)
}
