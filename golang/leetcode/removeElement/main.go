package main

import "fmt"

func removeElement(nums []int, val int) int {
	var index int
	for i := 0; i < len(nums); i++ {
		if nums[i] != val {
			if i != index {
				nums[index], nums[i] = nums[i], nums[index]
			}
			index++
		}
	}
	return index
}

func main() {
	var nums []int = []int{3, 2, 2, 3}
	var val int = 3
	fmt.Println(removeElement(nums, val))
}
