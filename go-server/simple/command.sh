#!/bin/bash

# Remove existing go.mod and go.sum files
# rm go.mod go.sum

# Initialize a new module
# go mod init your-module-name

# Re-add dependencies (list all your dependencies here)
go get -u github.com/gin-gonic/gin
# go get -u github.com/go-sql-driver/mysql

# Install all dependencies
go mod tidy

# Run the main.go file
go run main.go