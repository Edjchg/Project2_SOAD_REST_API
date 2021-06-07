package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func main() {

	// File to analyze.
	content, err := ioutil.ReadFile("pruebaPositivo.txt")

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(content))
}
