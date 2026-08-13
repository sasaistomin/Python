from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="public"))

@app.get("/")
def root():
    return FileResponse("public/index.html")

@app.get("/products")
def prod():
    return FileResponse("public/product.html")

@app.get("/con")
def con():
    return FileResponse("public/contacts.html")

@app.get('/about')
def about():
    return FileResponse("public/about.html")