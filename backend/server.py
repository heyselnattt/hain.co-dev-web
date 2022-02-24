from fastapi import FastAPI

app = FastAPI()


# === TESTING ===
@app.get('/')
def root():
    return {'message': 'Hello World'}


