package readtxt

import (
	"fmt"
	"io/ioutil"
	"log"
)

func readtxt(file string) {

	// File to analyze.
	content, err := ioutil.ReadFile(file)

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(content))
}
