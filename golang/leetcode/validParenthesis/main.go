package main

import "fmt"

func pop(stack []string) []string {
	return stack[:len(stack)-1]
}

func peek(stack []string) string {
	if len(stack) == 0 {
		return ""
	}
	return stack[len(stack)-1]
}

func isValid(s string) bool {
	var stack []string

	parenthesis := map[string]string{
		"(": ")",
		"[": "]",
		"{": "}",
	}

	for _, char := range s {
		charVal := string(char)

		if charVal == "(" || charVal == "[" || charVal == "{" {
			stack = append(stack, charVal)
		} else {
			last := peek(stack)
			if last == "" || parenthesis[last] != charVal {
				return false
			} else {
				stack = pop(stack)
			}
		}
	}

	return len(stack) == 0
}

func main() {
	s := "]"
	fmt.Println(isValid(s))
}
