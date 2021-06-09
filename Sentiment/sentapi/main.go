package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
)

type ResultAnalysis struct {
	Sentiment string `json:"sentiment"`
	Score     int    `json:"score"`
}

func main(pathFile string) {

	sentResult, scoreResult := sentapi(pathFile)

	body := &ResultAnalysis{
		Sentiment: sentResult,
		Score:     scoreResult,
	}

	buf := new(bytes.Buffer)
	json.NewEncoder(buf).Encode(body)
	req, _ := http.NewRequest("POST", "https://httpbin.org/post", buf)

	client := &http.Client{}
	res, e := client.Do(req)
	if e != nil {
		log.Fatal(e)
	}

	defer res.Body.Close()

	fmt.Println("response Status:", res.Status)

	// Print the body to the stdout
	io.Copy(os.Stdout, res.Body)
}
