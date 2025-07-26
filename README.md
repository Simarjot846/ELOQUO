# 🗣️ ELOQUO – Speak Freely, Heal Deeply

**Eloquo** is an AI-powered emotional companion that helps users express their feelings freely through voice input, while receiving thoughtful, empathetic responses. Whether you're anxious, stressed, or just need someone to talk to — Eloquo listens, understands, and supports.

## 🚀 What It Does

- 🎙️ **Voice-Based Input** – Speak your heart out instead of typing.
- 🧠 **Sentiment Analysis** – Understands your mood and emotional state.
- 💬 **Emotionally Aware Responses** – Gives replies that feel human, kind, and caring.
- 🪞 **Journaling + Reflection** – Automatically logs your conversations for self-reflection.
- 🎨 **Moodboard Generator** *(coming soon)* – Translates your mood into colors, music, or quotes.

## 💡 Inspiration

In a world full of noise, not everyone has someone to talk to. Eloquo was born out of the idea that **emotional release should be easy, non-judgmental, and accessible to all**.

## 🛠️ Tech Stack

| Layer        | Tech Used                                      |
|--------------|------------------------------------------------|
| **Frontend** | React Native / React.js / TypeScript (TSX)     |
| **Backend**  | Python (Flask API)                             |
| **AI Models**| OpenAI API, Google Speech-to-Text, MediaPipe   |
| **Demos**    | Gradio, Streamlit                              |


## 🧑‍💻 Made With Love By

- 🎯 **Simarjot Kaur**  
  *Sole Developer | UI/UX Designer | Creator of Eloquo*  
  > Built and implemented the full project independently — from idea to execution, including UI/UX, voice logic, AI integration, and final deployment.

- 🎥 **Ibrahim**  
  *Helped with video content, demo creation, and visuals.*

## 📂 How to Run It Locally

```bash
git clone https://github.com/yourusername/eloquo.git
cd ELOQUO
venv\Scripts\activate
pip install streamlit sounddevice scipy
pip install speechbrain
pip install opencv-python
pip install medipipe
streamlit run app.py
