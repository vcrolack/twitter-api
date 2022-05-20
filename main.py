from fastapi import FastAPI

app = FastAPI()


@app.get(path="/")
def home():
    return {"Twitter API": "Working"}






if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)