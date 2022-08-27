from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# localhost:8000/param-test/10?q=lol
# Returns {"Para Value": 10, "q": "lol"}
@app.get("/param-test/{para}")
def read_item(para: int, q: Union[str, None] = None):
    return {"Para Value": para, "q": q}
