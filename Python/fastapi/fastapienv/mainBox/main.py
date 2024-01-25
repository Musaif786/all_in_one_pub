from fastapi import FastAPI, File, UploadFile, HTTPException
from enum import Enum
from typing import Union
# from pydantic import BaseModel
from Model import model, post

app = FastAPI()

# class storingData(BaseModel):
#     name: str
#     num: int
#     desc: str

storingData = model.storingData
postdata = post.postData

@app.get("/")
async def hello():
    return {"Message": "hello world"}


@app.get("/item/{item_id}")
async def item(item_id):
    return {"ItemId": item_id, "Message": "Success"}

@app.get("/query")
async def query(name: list | str, id: Union[int, None]=None ):
    return {"Name": name, "ID": id }

@app.get("/query1")
async def query1(name: Union[str, None]=None, id: Union[int, None]=None ):
    return {"Name": name, "ID": id }


@app.post("/add")
async def addData(item: storingData):
    return {"Item": item}

@app.post("/post")
async def postData(item: postdata):
    return {"Item": item}


# file in bytes
@app.post("/file")
async def file_byte(file: bytes = File()):
    return {"FileSizeInMB": round(len(file)/1000,2)}

#upload file
@app.post("/file/upload")
async def file_upload(file: UploadFile):
    return {"File_details": file}


# error handler 
values = [9,10,11]
@app.get("/errorhandler/{item}")
async def errorfun(item: int):
    if item == 0 or item in values:
        return HTTPException(status_code=400, detail=f"{item} is not valied, Please take another value")
    return {"Item": item}