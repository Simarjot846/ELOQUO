def analyze_audio(file_path):
    import librosa
    import numpy as np

    y, sr = librosa.load(file_path)

    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch = pitches[magnitudes > np.median(magnitudes)]
    avg_pitch = np.mean(pitch) if len(pitch) > 0 else 0

    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    rms = librosa.feature.rms(y=y)[0]
    avg_energy = np.mean(rms)

    return {
        "Average Pitch (Hz)": round(avg_pitch, 2),
        "Speaking Speed (Beats/min)": round(float(tempo[0]), 2),
        "Volume/Energy Level": round(avg_energy, 4)
    }

