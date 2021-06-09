package main

import (
	"fmt"
	"log"

	"code.sajari.com/docconv"
)

func readDocx(file string) (content string) {
	res, err := docconv.ConvertPath(file)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf(res)
	return
}
