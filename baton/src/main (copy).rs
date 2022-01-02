use actix_cors::Cors;
use actix_files;
use actix_web::{get, post, http, web, App, HttpResponse, HttpServer, Responder};

const PORT:&str = "8001";
//const HOST:&str = "127.0.0.1"; -> for docker should be 0.0.0.0
const HOST:&str = "0.0.0.0";

#[actix_web::main]
async fn main() -> std::io::Result<()> {
	println!(">>> Server running on http://{}:{}...", HOST, PORT);
    HttpServer::new(|| {

        let _cors = Cors::default()
              .allowed_origin("https://www.rust-lang.org/")
              .allowed_origin_fn(|origin, _req_head| {
                  origin.as_bytes().ends_with(b".rust-lang.org")
              })
              .allowed_methods(vec!["GET", "POST"])
              .allowed_headers(vec![http::header::AUTHORIZATION, http::header::ACCEPT])
              .allowed_header(http::header::CONTENT_TYPE)
              .max_age(3600);

        App::new()
            .service(actix_files::Files::new("/", "./src/html").index_file("index.html"))
            //.service(actix_files::Files::new("/", "./react").index_file("index.html"))
            //.service(actix_files::Files::new("/", "././react").show_files_listing())
            //.service(Files::new("/static", std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("static")))
            //.service(index)
            //.service(echo)
            //.route("/hey", web::get().to(manual_hello))
    })
    .bind([HOST, PORT].join(":"))?
    .run()
    .await
}

/*#[get("/")]
async fn index() -> impl Responder {
    HttpResponse::Ok()
    .content_type("text/html; charset=utf-8")
    .body(include_str!("./../react/index.html"))
}

#[post("/echo")]
async fn echo(req_body: String) -> impl Responder {
    HttpResponse::Ok().body(req_body)
}

async fn manual_hello() -> impl Responder {
    HttpResponse::Ok().body("Hey there!")
}*/
