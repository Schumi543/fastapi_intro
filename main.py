from typing import Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get(
        "/items/{item_id}",
        response_model=Item,
        responses={
            200: {
                "content": {"image/png": {}},
                "description": "Return the JSON item or an image."
                }
            },
        )
def read_item(item_id: int, img: Optional[bool] = None, q: Optional[str] = None):
    if img:
        return FileResponse("image.png", media_type="image/png")
    else:
        return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items/")
async def create_item(item: Item):
    return item
