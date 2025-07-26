import streamlit as st
import sounddevice as sd
from scipy.io.wavfile import write
import os

from analyze_audio_utils import analyze_audio
from emotion_detector_utils import detect_emotion
from smile_eye_track_module import detect_smile_and_eyes_live_streamlit

# 🚀 Page Setup
st.set_page_config(page_title="Eloquo - Speech Coach", layout="centered")
st.title("🎙️ Eloquo - Your Public Speaking Coach")
st.markdown("Practice, record, and get instant AI-powered feedback on your speech.")

# 🧠 Initialize session state
if "webcam_analysis" not in st.session_state:
    st.session_state["webcam_analysis"] = None
if 'is_recording' not in st.session_state:
    st.session_state.is_recording = False

# 🎛️ Recording controls
minutes = st.slider("⏱️ Select Recording Duration (in minutes)", 1, 5, 2)
duration = minutes * 60
fs = 44100

# 🎤 Audio Recording
if not st.session_state.is_recording:
    if st.button("🎤 Start Recording"):
        st.session_state.is_recording = True
        st.info("Recording... Speak now.")
        st.session_state.audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
else:
    if st.button("⏹️ Stop Recording"):
        sd.wait()
        write("user_audio.wav", fs, st.session_state.audio)
        st.success("Recording complete! ✅")
        st.audio("user_audio.wav")
        st.session_state.is_recording = False

        # ✅ Audio Analysis
        with st.spinner("Analyzing audio..."):
            result = analyze_audio("user_audio.wav")
            st.subheader("📈 Speech Analysis")
            for key, value in result.items():
                st.write(f"**{key}:** {value}")

        # ✅ Emotion Detection
        with st.spinner("Detecting emotion..."):
            emotion_result = detect_emotion("user_audio.wav")
            if "Detected Emotion" in emotion_result:
                st.subheader("🎭 Emotion Detected")
                st.success(f"You sound: {emotion_result['Detected Emotion']}")
            else:
                st.error("❌ Could not detect emotion.")

        # ✅ Combined Feedback
        final_feedback = generate_feedback(result, emotion_result, st.session_state.webcam_analysis)
        st.subheader("💡 Personalized Feedback")
        for comment, quote in final_feedback:
            st.info(f"**{comment}**\n\n> _{quote}_")

# 📷 Smile & Eye Contact
with st.expander("📷 Live Smile & Eye Contact Detection"):
    if st.button("Start Live Webcam Analysis"):
        st.session_state.webcam_analysis = detect_smile_and_eyes_live_streamlit()

    if st.session_state.webcam_analysis:
        if st.session_state.webcam_analysis["eye_contact"]:
            st.success("✅ Good Eye Contact!")
        else:
            st.warning("👀 Try to maintain eye contact.")

        if st.session_state.webcam_analysis["smile"]:
            st.success("😊 You smiled! Great positivity!")
        else:
            st.warning("😐 Try smiling more during your speech.")

# 🔁 Reset Session
st.markdown("---")
if st.button("🔁 Reset Session"):
    st.session_state.clear()
    st.experimental_rerun()

# 💡 Feedback Function
def generate_feedback(result, emotion_result, face_result):
    feedback = []

    # 🗣️ Speaking Speed
    speed = result.get("Speaking Speed (Beats/min)", 0)
    if speed > 160:
        feedback.append(("You're speaking too fast. Try slowing down a bit.", "“Slow and steady wins the race.”"))
    elif speed < 80:
        feedback.append(("You're speaking quite slow. Add a bit more energy!", "“Let your energy fill the room.”"))
    else:
        feedback.append(("Your speaking speed is great!", "“Keep this rhythm—it’s working!”"))

    # 🎵 Pitch
    pitch = result.get("Average Pitch (Hz)", 0)
    if pitch < 120:
        feedback.append(("Your voice is a bit flat. Try adding more vocal variation.", "“Your voice is your music—make it expressive.”"))
    elif pitch > 300:
        feedback.append(("Your pitch is a bit high. Relax and ground your voice.", "“Calm confidence speaks loudest.”"))
    else:
        feedback.append(("Good pitch range. Your voice sounds confident!", "“Confidence isn’t loud—it’s consistent.”"))

    # 🎭 Emotion
    emotion = emotion_result.get("Detected Emotion", "")
    if emotion:
        feedback.append((f"Your emotion was detected as **{emotion}**.", "“Let your feelings flow through your words.”"))

    # 👀 Eye Contact
    if face_result:
        if face_result.get("eye_contact"):
            feedback.append(("✅ Good eye contact detected!", "“Eyes are the windows to connection.”"))
        else:
            feedback.append(("👀 Improve your eye contact for better engagement.", "“Look your audience in the eyes—they’ll listen.”"))

        # 😀 Smile
        if face_result.get("smile"):
            feedback.append(("😊 You smiled—great energy and warmth!", "“A smile is your superpower on stage.”"))
        else:
            feedback.append(("😐 Try smiling more—it boosts trust and impact.", "“Smile—it’s the shortcut to connection.”"))

    return feedback

