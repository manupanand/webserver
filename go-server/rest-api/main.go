package main
import (
	"fmt"
	"net/http"
	"github.com/gin-gonic/gin"
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
func getTodo(context *gin.Context){
	context.JSON(http.StatusOK,todos)

}
func addTodo(context *gin.Context){
	var newTodo todo//type of todo
	//post request -get data -in JSON inrequest body -BindJSON
	if err := context.BindJSON(&newTodo); err != nil{
		context.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return 
	}
	//add todos to list
	todos = append(todos,newTodo)
	context.JSON(http.StatusCreated,newTodo)
}
// clen and server communicate use JSON-decalre inside struct
func main(){
	fmt.Println("test")
	//server assign variable-router is server
	router:=gin.Default()
	//create enpoint-get("path",function)-function which return json data
	router.GET("/todos",getTodo)
	//post
	router.POST("/todos",addTodo)
	//run server -router.Run()
	router.Run("localhost:9090")
	// fmt.Println("test")
}

//to download the package 
// go get github.com/gin-conic/gin