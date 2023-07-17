package main

import "fmt"

func strStr(haystack string, needle string) int {

	needleLength := len(needle)
	haystackLength := len(haystack)

	for i, _ := range haystack {
		if i+needleLength > haystackLength {
			return -1
		} else if haystack[i:i+needleLength] == needle {
			return i
		}
	}
	return -1
}

func main() {
	var haystack string = "aaa"
	var needle string = "aaaa"

	fmt.Println(strStr(haystack, needle))
}
