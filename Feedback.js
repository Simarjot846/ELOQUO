import React, { useState } from 'react';
import axios from 'axios';

export default function Feedback() {
  const [tone, setTone] = useState('');
  const [emotion, setEmotion] = useState('');
  const [feedback, setFeedback] = useState('');

  const handleSubmit = async () => {
    const res = await axios.post('http://localhost:8000/analyze', {
      tone, emotion
    });
    setFeedback(res.data);
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Get Feedback</h2>
      <input type="text" value={tone} onChange={e => setTone(e.target.value)} placeholder="Tone (e.g., nervous)" />
      <input type="text" value={emotion} onChange={e => setEmotion(e.target.value)} placeholder="Emotion (e.g., happy)" />
      <button onClick={handleSubmit} className="bg-purple-500 text-white px-4 py-2 mt-2">Analyze</button>
      
      {feedback && (
        <div className="mt-4 bg-gray-100 p-4 rounded">
          <p><strong>Tone Feedback:</strong> {feedback.tone_feedback}</p>
          <p><strong>Emotion Feedback:</strong> {feedback.emotion_feedback}</p>
        </div>
      )}
    </div>
  );
}
