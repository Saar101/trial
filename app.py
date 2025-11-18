from fastapi import FastAPI

app = FastAPI()

@app.get("/endpoint")
async def first_api():
    return {"message": "Hello saar!"}