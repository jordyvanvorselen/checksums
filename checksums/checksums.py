from fastapi import FastAPI

app = FastAPI()


@app.post("/checksums")
async def checksums():
    return {"checksum": "a3423j4jk23h423bh4324jb23h4234kj234"}
