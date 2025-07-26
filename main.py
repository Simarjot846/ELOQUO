from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from feedback_utils import analyze_tone_emotion

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to frontend domain in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    tone = data.get("tone", "")
    emotion = data.get("emotion", "")
    feedback = analyze_tone_emotion(tone.lower(), emotion.lower())
    return feedback

@app.get("/")
def read_root():
    return {"Hello": "World"}
