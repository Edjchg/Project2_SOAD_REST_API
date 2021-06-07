package readDocx

import (
	"fmt"
	"log"

	"code.sajari.com/docconv"
)

func readDocx(file string) {
	res, err := docconv.ConvertPath(file)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(res)
}
