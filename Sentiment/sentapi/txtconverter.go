package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func readtxt(file string) (content string) {

	// File to analyze.
	res, err := ioutil.ReadFile(file)

	if err != nil {
		log.Fatal(err)
	}
	content = string(res)
	return content
	fmt.Println(string(res))
}
