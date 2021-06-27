package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"

	"github.com/gocolly/colly"
)

func main() {

	file, err := os.Create("csvfile.csv")
	if err != nil {
		log.Fatalf("failed creating file: %s", err)
		return
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	c := colly.NewCollector(
		colly.AllowedDomains("justdial.com"),
	)

	c.OnHTML("h2.store-name", func(e *colly.HTMLElement) {
		/*writer.Write([]string{
			e.ChildText("a[href]"),
			e.ChildText("a"),
		})*/
		fmt.Println("visiting")
	})

	c.OnRequest(func(e *colly.Request) {
		fmt.Println("Visiting")
	})

	c.Visit("https://www.justdial.com/Delhi/Restaurants-in-Indirapuram/nct-10408936")
	fmt.Print("complete")
}

//var URL string
//var csvfile string

//reader := bufio.NewReader(os.Stdin)

//to collect input
//fmt.Println("Please enter the URL")
//URL, _ = reader.ReadString('\n')
//fmt.Println(URL)
//fmt.Println("Please enter the name of file")
//csvfile, _ = reader.ReadString('\n')

//csvfile1 := csvfile + ".csv"
//fmt.Println(URL)
//fmt.Println(csvfile)
//csv file name
