package main

import "fmt"

func lengthOfLastWord(s string) int {
	var count int = 0

	for i := len(s) - 1; i >= 0; i-- {
		if string(s[i]) == " " {
			if count > 0 {
				break
			}
		} else {
			count++
		}
	}
	return count
}

func main() {
	s := "Hello World"
	fmt.Println(lengthOfLastWord(s))
}
