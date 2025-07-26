def analyze_speech_transcript(transcript):
    if "uh" in transcript or "um" in transcript:
        return "Try reducing filler words for more clarity."
    elif "sorry" in transcript:
        return "Avoid apologizing too much while speaking."
    else:
        return "Good fluency! Try adding emphasis for better impact."
