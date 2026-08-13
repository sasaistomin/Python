# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# from fastapi.responses import FileResponse
# from fastapi.staticfiles import StaticFiles

# app = FastAPI()
# app.mount("/static", StaticFiles(directory="public", html=True))

# @app.get("/")
# def read_root():
#     # html_content = "<h2>Hello World</h2>"
#     # return HTMLResponse(content=html_content)
#     return FileResponse(path="public/index.html", media_type="text/html")

# @app.get("/about")
# def about():
#     return FileResponse(path="public/about.html", media_type="text/html")

# @app.get("/user/{id}/{name}")
# def user(id, name):
#     return {'user_id': id, "user_name": name}


from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="public"))

@app.get("/")
def root():
    return FileResponse("public/index.html")

@app.post("/hello")
#def hello(name = Body(embed=True)):
def hello(data = Body()):
    name = data["name"]
    age = data["age"]
    return {"message": f"{name}, ваш возраст - {age}"}