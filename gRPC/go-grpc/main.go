package main

import (
	"github.com/gofiber/fiber/v2"
)

func handler(c *fiber.Ctx) error {
	return c.SendString("test server")
}
func main() {
	app := fiber.New()

	app.Get("/", handler)
	app.Listen(":3000")
}
