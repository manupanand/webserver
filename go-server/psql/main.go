package main

import (
    "database/sql"
    "fmt"
    "log"

    _ "github.com/lib/pq"
)

func main() {
    connStr := "user=username password=yourpassword dbname=yourdb sslmode=disable"
    db, err := sql.Open("postgres", connStr)
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    err = db.Ping()
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Successfully connected!")

    var result string
    err = db.QueryRow("SELECT some_column FROM some_table LIMIT 1").Scan(&result)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result)
}