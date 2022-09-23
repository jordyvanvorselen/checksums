import hashlib
from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.post("/checksums")
async def checksums(file: UploadFile):
    file_content = await file.read()
    checksum = hashlib.md5(file_content).hexdigest()
    return {"checksum": checksum}
