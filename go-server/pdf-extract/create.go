package main

import (
	"github.com/jung-kurt/gofpdf"
)

func main() {
	pdf := gofpdf.New("P", "mm", "A4", "")
	pdf.AddPage()

	pdf.SetFont("Arial", "B", 16)
	pdf.Cell(40, 10, "Hello, World!")

	err := pdf.OutputFileAndClose("newfile.pdf")
	if err != nil {
		panic(err)
	}
}