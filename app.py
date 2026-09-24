from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to Student Management API!",
        "status": "success"
    }

@app.get("/courses")
def courses():
    return {
        "courses": [
            {"id": 1, "name": "MSc IT"},
            {"id": 2, "name": "MSc Data Science"},
            {"id": 3, "name": "MCA"}
        ]
    }

@app.get("/college")
def college():
    return {
        "college": "ABC College",
        "location": "Mumbai",
        "university": "Mumbai University"
    }