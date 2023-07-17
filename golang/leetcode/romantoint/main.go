package main

import "fmt"

func romanToInt(s string) int {
	romans := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}

	result := 0

	var index int = 0
	var length int = len(s)

	for index < length {
		numChar := string(s[index])

		if index == length-1 {
			result += romans[numChar]
			break
		}

		nextNumChar := string(s[index+1])

		if romans[nextNumChar] > romans[numChar] {
			result = result + romans[nextNumChar] - romans[numChar]
			index += 2
		} else {
			result += romans[numChar]
			index += 1
		}

	}

	return result
}

func main() {
	fmt.Println(romanToInt("MCMXCIV"))
}
