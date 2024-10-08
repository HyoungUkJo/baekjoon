package main

import (
    "fmt"
    "strconv"
)

func main() {
    var N int
    var numStr string
    var sum int = 0

    fmt.Scan(&N)

    fmt.Scan(&numStr)

    for i := 0; i < N; i++ {
        num, _ := strconv.Atoi(string(numStr[i]))
        sum += num
    }

    // 결과 출력
    fmt.Println(sum)
}