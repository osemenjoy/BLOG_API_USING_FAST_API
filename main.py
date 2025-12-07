from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Decorate to give the url for the api
def index():
    return {"data": {"Message":"Hello, World!", "status_code": 200}}


@app.get("/blog")
def blog(limit=10, published: bool=True):

    if published:
        return {
            "data": f"{limit} published blogs from the db"
        }
    else:
        return {
            "data": f"{limit} blogs from the db"
        }
@app.get("/about")
def about_page():
    return {
        "data": {
            "message": "About API created successfully",
            "status code": 200
        }
    }


@app.get("/blog/{id}")
def get_about(id: int):
    return {"data": id}