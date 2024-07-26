package main

import (
	"fmt"
	"log"

	"github.com/pdfcpu/pdfcpu/pkg/api"
	"github.com/pdfcpu/pdfcpu/pkg/pdfcpu"
)

func main() {
	filePath := "sample.pdf"
	config := pdfcpu.NewDefaultConfiguration()

	content, err := api.ExtractTextFile(filePath, nil, config)
	if err != nil {
		log.Fatalf("Error extracting text: %v", err)
	}

	fmt.Println(content)
}