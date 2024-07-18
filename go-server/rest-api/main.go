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
//function which take parameter whic 10- https://www.youtube.com/watch?v=d_L64KT3SFM
fun getTodo(context *){

}
// clen and server communicate use JSON-decalre inside struct
func main(){
	//server assign variable-router is server
	router:=gin.Default()
	//create enpoint-get("route",function)-function which return json data
	router.GET("/todos",)
	//run server -router.Run()
	router.Run("localhost:9090")
	// fmt.Println("test")
}

//to download the package 
// go get github.com/gin-conic/gin