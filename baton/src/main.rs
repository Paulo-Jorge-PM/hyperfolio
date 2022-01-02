//use actix_cors::Cors;
//use actix_files;
use actix_web::{get, post, http, web, App, HttpResponse, HttpServer, Responder};

use actix_web::{web, App, HttpServer, HttpRequest, HttpResponse, Responder};
use tera::{Tera, Context};

const PORT:&str = "8001";
//const HOST:&str = "127.0.0.1"; -> for docker should be 0.0.0.0
const HOST:&str = "0.0.0.0";

fn index() -> impl Responder {
    HttpResponse::Ok().body("hello world!")
}

struct AppData {
    tmpl: Tera
}

fn main() {
    HttpServer::new(|| {
        let tera =
            Tera::new(
                concat!(env!("CARGO_MANIFEST_DIR"), "/templates/**/*")
            ).unwrap();

        App::new()
            .data(AppData {tmpl: tera})
            .service(
                web::resource("/")
                    .route(web::get().to(index))
            )
            /*.service(
                web::resource("/users")
                    .route(web::get().to(get_users))
                    .route(web::put().to(put_users))
            )
            .service(
                web::resource("/hello/{name}")
                    .route(web::get().to(say_hello))
            )
            .service(
                web::resource("/tmpl/{name}")
                    .route(web::get().to(render_tmpl))
            )*/
    })
    .bind([HOST, PORT].join(":"))?
    .unwrap()
    .run()
    .unwrap();
}


/*
#[actix_web::main]
async fn main() -> std::io::Result<()> {
	println!(">>> Server running on http://{}:{}...", HOST, PORT);
    HttpServer::new(|| {

        let tera =
            Tera::new(
                concat!(env!("CARGO_MANIFEST_DIR"), "/templates/**/*")
            ).unwrap();

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
            //.service(actix_files::Files::new("/", "./src/html").index_file("index.html"))
            //.service(actix_files::Files::new("/", "./react").index_file("index.html"))
            //.service(actix_files::Files::new("/", "././react").show_files_listing())
            //.service(Files::new("/static", std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("static")))
            .service(
                web::resource("/")
                    .route(web::get().to(index))
            )
            //.service(echo)
            //.route("/hey", web::get().to(manual_hello))
    })
    .bind([HOST, PORT].join(":"))?
    .run()
    .await
}*/

/*
fn index() -> impl Responder {
    HttpResponse::Ok().body("hello world!")
}*/

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
