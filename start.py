import uvicorn
from fastapi import FastAPI
from web.routes import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"message": "AI Network Security Gateway Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
