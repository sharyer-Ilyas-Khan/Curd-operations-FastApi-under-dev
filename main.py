
from fastapi import FastAPI

app = FastAPI()

@app.get("/get/")
async def showName():
    return "Sharyer"