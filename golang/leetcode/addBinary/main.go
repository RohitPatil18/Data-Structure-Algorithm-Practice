package main

import "fmt"

func adder(a string, b string, carry string) (string, string) {
	if carry == "1" {
		if a == "1" && b == "1" {
			return "1", "1"
		} else if (a == "1" && b == "0") || (a == "0" && b == "1") {
			return "0", "1"
		} else {
			return "1", "0"
		}
	} else {
		if a == "1" && b == "1" {
			return "0", "1"
		} else if (a == "1" && b == "0") || (a == "0" && b == "1") {
			return "1", "0"
		} else {
			return "0", "0"
		}
	}
	return "0", "0"
}

func getResult(str string, idx int, carry string, result string) (string, string) {
	res := ""

	for idx >= 0 {
		res, carry = adder("0", string(str[idx]), carry)
		result = res + result
		idx--
	}
	return result, carry
}

func addBinary(a string, b string) string {
	idxA := len(a) - 1
	idxB := len(b) - 1

	result := ""

	carry := "0"
	res := ""

	for {
		if idxA > -1 && idxB > -1 {
			res, carry = adder(string(a[idxA]), string(b[idxB]), carry)
			result = res + result
			idxA--
			idxB--
		} else if idxA == -1 && idxB == -1 {
			break
		} else if idxA > -1 {
			result, carry = getResult(a, idxA, carry, result)
			idxA = -1
		} else {
			result, carry = getResult(b, idxB, carry, result)
			idxB = -1
		}
	}

	if carry == "1" {
		result = "1" + result
	}
	return result
}

func main() {
	a := "11"
	b := "1"
	fmt.Println(addBinary(a, b))
}
