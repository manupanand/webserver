package main

import (
	"fmt"
	"log"

	"github.com/jung-kurt/gofpdf"
	"github.com/pdfcpu/pdfcpu/pkg/api"
	"github.com/pdfcpu/pdfcpu/pkg/pdfcpu"
)

func main() {
	// Reading from an existing PDF
	filePath := "sample.pdf"
	config := pdfcpu.NewDefaultConfiguration()

	content, err := api.ExtractTextFile(filePath, nil, config)
	if err != nil {
		log.Fatalf("Error extracting text: %v", err)
	}

	fmt.Println("Extracted Text:", content)

	// Creating a new PDF with the extracted content
	pdf := gofpdf.New("P", "mm", "A4", "")
	pdf.AddPage()
	pdf.SetFont("Arial", "B", 16)

	pdf.MultiCell(0, 10, content, "", "", false)

	err = pdf.OutputFileAndClose("newfile.pdf")
	if err != nil {
		log.Fatalf("Error creating PDF: %v", err)
	}

	fmt.Println("New PDF created successfully.")
}
