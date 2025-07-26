from speechbrain.pretrained.interfaces import foreign_class
import torch

def detect_emotion(file_path):
    try:
        classifier = foreign_class(
            source="speechbrain/emotion-recognition-wav2vec2-IEMOCAP",
            pymodule_file="custom_interface.py",
            classname="CustomEncoderClassifier"
        )
    except Exception as e:
        return {"error": str(e)}