from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    response = {"message": "API is running!"}
    return JSONResponse(content=response, status_code=202)
