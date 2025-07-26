import random

def analyze_tone_emotion(tone: str, emotion: str):
    # Your analysis logic here
    return {"feedback": f"Tone: {tone}, Emotion: {emotion}"}

def analyze_posture_score(score):
    if score > 80:
        return "Your posture looks confident and professional!"
    elif score > 60:
        return "Decent posture, but try to stand a bit straighter."
    else:
        return "Posture needs improvement. Avoid slouching and stay upright."


def generate_full_feedback(tone, emotion, posture_score):
    tone_emotion = analyze_tone_emotion(tone, emotion)
    posture = analyze_posture_score(posture_score)

    return {
        "tone_feedback": tone_emotion["tone_feedback"],
        "emotion_feedback": tone_emotion["emotion_feedback"],
        "posture_feedback": posture
    }
    