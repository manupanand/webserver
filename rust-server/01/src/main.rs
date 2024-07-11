use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
struct MyObj {
    name: String,
    number: i32,
}

#[get("/")]
async fn hello() -> impl Responder {
    HttpResponse::Ok().json(MyObj {
        name: "Hello, World!".to_string(),
        number: 42,
    })
}

#[post("/echo")]
async fn echo(req_body: String) -> impl Responder {
    HttpResponse::Ok().body(req_body)
}

#[get("/health")]
async fn health_check() -> impl Responder {
    HttpResponse::Ok().body("Healthy")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(hello)
            .service(echo)
            .service(health_check)
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}