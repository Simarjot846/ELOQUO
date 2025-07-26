import cv2
import numpy as np
import mediapipe as mp
import streamlit as st

def detect_smile_and_eyes_live_streamlit():
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False)
    cap = cv2.VideoCapture(0)

    stframe = st.empty()
    feedback_placeholder = st.empty()

    stop = False
    stop_button = st.button("🛑 Stop Analysis")

    while cap.isOpened() and not stop:
        ret, frame = cap.read()
        if not ret:
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)

        smile = False
        eye_contact = False

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # EAR (Eye Aspect Ratio)
                left_eye = [33, 160, 158, 133, 153, 144]
                right_eye = [362, 385, 387, 263, 373, 380]

                def ear(eye_points):
                    def p(index): return np.array([face_landmarks.landmark[index].x,
                                                    face_landmarks.landmark[index].y])
                    vertical1 = np.linalg.norm(p(eye_points[1]) - p(eye_points[5]))
                    vertical2 = np.linalg.norm(p(eye_points[2]) - p(eye_points[4]))
                    horizontal = np.linalg.norm(p(eye_points[0]) - p(eye_points[3]))
                    return (vertical1 + vertical2) / (2.0 * horizontal)

                ear_left = ear(left_eye)
                ear_right = ear(right_eye)
                avg_ear = (ear_left + ear_right) / 2.0

                eye_contact = avg_ear > 0.25  # Threshold

                # Dummy smile detection (basic logic - you can enhance this)
                top_lip = face_landmarks.landmark[13].y
                bottom_lip = face_landmarks.landmark[14].y
                mouth_open = bottom_lip - top_lip
                smile = mouth_open > 0.03  # Threshold

        # Show result on frame
        status_text = []
        if eye_contact:
            status_text.append("✅ Eye Contact")
        else:
            status_text.append("👀 Open your eyes")

        if smile:
            status_text.append("😊 Nice Smile")
        else:
            status_text.append("😐 Try smiling")

        y0 = 30
        for text in status_text:
            cv2.putText(frame, text, (10, y0), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            y0 += 30

        # Show video feed
        stframe.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB", use_container_width=True)

        # Show feedback text
        feedback_placeholder.markdown("**Live Feedback:**<br>" + "<br>".join(status_text), unsafe_allow_html=True)

        # Check if stop button is pressed
        if st.session_state.get("stop_live", False) or stop_button:
            stop = True

    cap.release()
    return {"smile": smile, "eye_contact": eye_contact}




