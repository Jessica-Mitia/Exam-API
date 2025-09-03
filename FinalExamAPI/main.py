from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response, JSONResponse

app = FastAPI()

@app.get("/health")
def isOk():
    return Response(content="Ok", status_code=200)

class Characteristic(object):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

phones_store: List[Phone] = []

def serialized_phone():
    serialized_phone_ok = []
    for phone in phones_store:
        serialized_phone_ok.append(phone.model_dump())
    return serialized_phone_ok

@app.post('/phones')
def create_list(phones: List[Phone]):
    phones_store.extend(phones)
    return JSONResponse(content=serialized_phone(), status_code=201, media_type="appliaction/json")
@app.get('/phones')
def list_phone():
    return JSONResponse(content=serialized_phone(), status_code=200, media_type="application/json")

@app.get('/phones/{id}')
def getPhoneById(id: int):
    for phone in phones_store:
        if phone.identifier == id:
            return JSONResponse(content=phone, status_code=200, media_type="application/json")
    return JSONResponse(content={"error" : "phone not found"}, status_code=404)

@app.put('/phones/{id}/characteristic')
def changeCharacteristics(new_characteristic: Characteristic, id: int):
    for phone in phones_store:
        if phone.identifier == id:
            phone.characteristics = new_characteristic
    return JSONResponse(content=phone, status_code=200)





