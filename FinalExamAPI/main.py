from fastapi import FastAPI
from starlette.responses import Response, JSONResponse

app = FastAPI()

@app.get("/ping")
def pong():
    return JSONResponse(content={"message" : "pong"}, status_code=200)
