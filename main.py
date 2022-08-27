from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/param-test/{para}")
def read_item(para: int, q: Union[str, None] = None):
    return {"Your Paramater was:": para, "q": q}
