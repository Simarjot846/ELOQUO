def generate_score(voice_speed, emotion, eye, smile):
    score = 0
    tips = []

    # Voice Speed
    if 130 <= voice_speed <= 180:
        score += 25
    else:
        tips.append("Adjust your speech speed to sound more natural.")

    # Emotion
    if emotion in ['happy', 'calm']:
        score += 25
    else:
        tips.append("Try to sound more positive and relaxed.")

    # Eye contact
    if eye:
        score += 25
    else:
        tips.append("Maintain eye contact for better connection.")

    # Smile
    if smile:
        score += 25
    else:
        tips.append("Smile a bit to sound more confident and friendly.")

    return score, tips
