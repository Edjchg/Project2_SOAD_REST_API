package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

type ResultAnalysis struct {
	Sentiment string  `json:"sentiment"`
	Score     float32 `json:"score"`
	FileName  string  `json:"filename"`
}

func main() {

	filename := initReceiver()

	//Get the path of where is located the file
	pwd, err := os.Getwd()
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(pwd)
	// Change "filesTest" for "TEMP_FILE"
	path := pwd + "/" + "tmp" + filename

	sentResult, scoreResult := sentapi(path)
	//fmt.Printf(sentResult, scoreResult)

	result := &ResultAnalysis{
		Sentiment: sentResult,
		Score:     scoreResult,
		FileName:  filename,
	}

	fmt.Println("Body Json: ", result)

	b, err := json.Marshal(result)
	if err != nil {
		fmt.Printf("Error: %s", err)
		return
	}
	fmt.Println(string(b))

	fmt.Println("Header Json: ", result)

	req, e := http.NewRequest("GET", "/sentimentInsert/", nil)
	if err != nil {
		log.Fatal(e)
	}
	req.Header.Set("Content-Type", "application/json")
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Body: ", body)

	//POST to Mongo API with the result of the analysis

	/*buf := new(bytes.Buffer)
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
	io.Copy(os.Stdout, res.Body)*/
}
