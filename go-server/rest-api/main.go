package main
import (
	"fmt"
	"net/http"
	"github.com/gin-conic/gin"
)
//define the structure of data
type todo struct{
	ID			string `json:"id"`
	Item		string	`json:"title"`
	Completed	bool	`json:"completed"`
}
//todos array
var todos = []todo{
	{ID:"1",Item :"Clean Room", Completed:false},
	{ID:"2",Item :"watch movie", Completed:false},
	{ID:"3",Item :"gym", Completed:false},
}
//function which take parameter which is type-gin.Context
//extract inconme data-extract from context-tranform todos into  JSON,1-status-http
fun getTodo(context *gin.Context){
	context.IntendedJSON(http.StatusOK,todos)

}
// clen and server communicate use JSON-decalre inside struct
func main(){
	//server assign variable-router is server
	router:=gin.Default()
	//create enpoint-get("path",function)-function which return json data
	router.GET("/todos",getTodo(todos))
	//run server -router.Run()
	router.Run("localhost:9090")
	// fmt.Println("test")
}

//to download the package 
// go get github.com/gin-conic/gin