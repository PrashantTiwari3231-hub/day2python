from fastapi import FastAPI
app =FastAPI()

@app.get("/")
def home():
    return {"message": "cyber toolkit API"}

@app.get("/challenge/{challenge_id}")
def get_challenge(challenge_id: int):
    return{
        "id":challenge_id,
        "name":"forensic challenge",
        "difficulty":"beginner"
    }

@app.post("/challenge")
def create_challenge(name:str, difficulty:str):
    return{
        "name":name,
        "difficulty":difficulty
    }


