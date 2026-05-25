from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}
@app.get("/teste")
def teste():
    return {"message": "Teste"}