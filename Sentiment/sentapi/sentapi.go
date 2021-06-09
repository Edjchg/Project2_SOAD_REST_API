/*package main

import (
	"context"
	"fmt"
	"log"
	"path/filepath"

	language "cloud.google.com/go/language/apiv1"
	languagepb "google.golang.org/genproto/googleapis/cloud/language/v1"
)

func getContent(pathFile string) (content string) {

	fileExtension := filepath.Ext(pathFile)

	if fileExtension == "pdf" {
		content := ReadPlainTextFromPDF(pathFile)
	} else if fileExtension == "txt" {
		content := ReadPlainTextFromPDF(pathFile)
	} else {
		content := ReadPlainTextFromPDF(pathFile)
	}

	fmt.Println("File extension ", fileExtension)
}

func sentapi(pathFile string) (sentimentResult string, scoreResult int) {

	content := getContent(pathFile)

	ctx := context.Background()

	// Creates a client.
	client, err := language.NewClient(ctx)
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}
	defer client.Close()

	// Detects the sentiment of the text.
	sentiment, err := client.AnalyzeSentiment(ctx, &languagepb.AnalyzeSentimentRequest{
		Document: &languagepb.Document{
			Source: &languagepb.Document_Content{
				Content: content,
			},
			Type: languagepb.Document_PLAIN_TEXT,
		},
		EncodingType: languagepb.EncodingType_UTF8,
	})
	if err != nil {
		log.Fatalf("Failed to analyze text: %v", err)
	}

	fmt.Printf("Text: %v\n", string(content))
	scoreResult = sentiment.DocumentSentiment.Score
	if sentiment.DocumentSentiment.Score >= 0 {
		sentimentResult = "Positive"
		fmt.Println("Sentiment: positive")
	} else {
		sentimentResult = "Positive"
		fmt.Println("Sentiment: negative")
	}
	return
}*/

package main

import (
	"context"
	"fmt"
	"io/ioutil"
	"log"

	language "cloud.google.com/go/language/apiv1"
	languagepb "google.golang.org/genproto/googleapis/cloud/language/v1"
)

func main() {
	ctx := context.Background()

	// File to analyze.
	content, err := ioutil.ReadFile("pruebaNegativo.txt")

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(content))

	// Creates a client.
	client, err := language.NewClient(ctx)
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}
	defer client.Close()

	// Detects the sentiment of the text.
	sentiment, err := client.AnalyzeSentiment(ctx, &languagepb.AnalyzeSentimentRequest{
		Document: &languagepb.Document{
			Source: &languagepb.Document_Content{
				Content: string(content),
			},
			Type: languagepb.Document_PLAIN_TEXT,
		},
		EncodingType: languagepb.EncodingType_UTF8,
	})
	if err != nil {
		log.Fatalf("Failed to analyze text: %v", err)
	}

	fmt.Printf("Text: %v\n", string(content))
	if sentiment.DocumentSentiment.Score >= 0 {
		fmt.Println("Sentiment: positive", sentiment.DocumentSentiment.Score)
	} else {
		fmt.Println("Sentiment: negative", sentiment.DocumentSentiment.Score)
	}
}
