from fastapi import FastAPI

app = FastAPI()

@app.get("/fastapi")
def home():
    return {"message": "Hello from FastAPI App!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5002)
