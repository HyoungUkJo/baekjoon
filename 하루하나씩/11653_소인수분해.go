package main

import "fmt"

func main(){
	var N int
	var i int = 2

	_, err:=fmt.Scan(&N)

	if err!=nil{
		fmt.Println("error")
		return
	}

	for N!=1{
		if N==0{
			break;
		}
		if N%i==0{
			fmt.Println(i)
			N=N/i
		} else {
			i++
		}
	}
}