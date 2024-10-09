package main

import (
	"fmt"
	"strconv"
)

func main() {
	var N string
	fmt.Scan(&N)

	if len(N)>1 && N[0:2] == "0x" {
		i16,_ := strconv.ParseInt(N, 0, 64)
		fmt.Print(i16)
	} else if len(N)>1 && N[0:1] == "0" {
		i8,_ := strconv.ParseInt(N, 0, 64)
		fmt.Print(i8)
	} else {
		i10,_ := strconv.ParseInt(N, 0, 64)
		fmt.Print(i10)
	}
}