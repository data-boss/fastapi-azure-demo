from fastapi import FastAPI

app = FastAPI()
uvicorn main:app --host 0.0.0.0 --port 8000

@app.get("/")
def read_root():
    return {"message": "Hello from Azure!"}
