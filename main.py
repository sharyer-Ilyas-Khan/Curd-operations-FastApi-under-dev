import json
from typing import Union

from fastapi import FastAPI
from fastapi import Response
from pydantic import BaseModel
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        # return {"model_name": model_name, "message": "Deep Learning FTW!"}
        return json.JSONEncoder(default={"model_name": model_name, "message": "Deep Learning FTW!"})

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
