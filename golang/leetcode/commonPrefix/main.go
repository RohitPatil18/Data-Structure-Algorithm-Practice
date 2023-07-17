package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	var common string

	index := 0

	stopIteration := false
	for {
		char := ""
		isCommon := true
		for _, str := range strs {
			if len(str) == index {
				stopIteration = true
				break
			}

			if char == "" {
				char = string(str[index])
			} else {
				if char != string(str[index]) {
					isCommon = false
					stopIteration = true
					break
				}
			}

		}

		if stopIteration {
			break
		}

		if isCommon {
			common += char
		}
		index += 1
	}
	return common
}

func main() {
	var strs []string = []string{"cir", "car"}
	fmt.Println(longestCommonPrefix(strs))
}
