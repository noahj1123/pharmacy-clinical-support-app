form fastapi import FastApi

app = FastAPI()

@app.get("/")

def home():
    return {"message": "Pharmacy Clinical Support API is running"}
    