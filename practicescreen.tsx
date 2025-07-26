// src/screens/PracticeSpeechScreen.tsx
import React, { useState } from 'react';
import { View, Text, Button, TouchableOpacity, StyleSheet } from 'react-native';
import { Audio } from 'expo-av';
import { useNavigation } from '@react-navigation/native';
type RootStackParamList = {
  PracticeSpeechScreen: undefined;
  FeedbackScreen: { audioUri: string | null };
};

export default function PracticeSpeechScreen() {
  const [recording, setRecording] = useState<Audio.Recording | null>(null);
  const [recordedUri, setRecordedUri] = useState<string | null>(null);
  const navigation = useNavigation<import('@react-navigation/native').NavigationProp<RootStackParamList>>();

  const startRecording = async () => {
    try {
      console.log('Requesting permissions..');
      await Audio.requestPermissionsAsync();
      await Audio.setAudioModeAsync({
        allowsRecordingIOS: true,
        playsInSilentModeIOS: true,
      });

      console.log('Starting recording..');
      const recordingOptions = {
        android: {
          extension: '.m4a',
          outputFormat: 2, // MPEG_4
          audioEncoder: 3, // AAC
          sampleRate: 44100,
          numberOfChannels: 2,
          bitRate: 128000,
        },
        ios: {
          extension: '.m4a',
          audioQuality: 'high',
          sampleRate: 44100,
          numberOfChannels: 2,
          bitRate: 128000,
          linearPCMBitDepth: 16,
          linearPCMIsBigEndian: false,
          linearPCMIsFloat: false,
        },
        web: {
          mimeType: 'audio/webm',
          bitsPerSecond: 128000,
        },
      };
      const { recording } = await Audio.Recording.createAsync(
        Audio.RecordingOptionsPresets.HIGH_QUALITY
      );
      setRecording(recording);
      console.log('Recording started');
    } catch (err) {
      console.error('Failed to start recording', err);
    }
  };

  const stopRecording = async () => {
    console.log('Stopping recording..');
    if (recording) {
      await recording.stopAndUnloadAsync();
      const uri = recording.getURI();
      console.log('Recording stopped and stored at', uri);
      setRecordedUri(uri);
      setRecording(null);
    }
  };

  const handleUpload = () => {
    // navigation or logic to feedback
    navigation.navigate('FeedbackScreen', { audioUri: recordedUri });
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Practice Your Speech</Text>

      <TouchableOpacity
        style={styles.button}
        onPress={recording ? stopRecording : startRecording}>
        <Text style={styles.buttonText}>
          {recording ? 'Stop Recording' : 'Start Recording'}
        </Text>
      </TouchableOpacity>

      {recordedUri && (
        <Button title="Get Feedback" onPress={handleUpload} />
      )}
    </View>
  );
}
const PracticeScreen = () => {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Practice Your Speech</h1>

      {/* 🎥 Your video/audio recorder goes here */}

      {/* ✅ Feedback Section */}
      <View style={{ marginTop: 16, backgroundColor: '#fff', borderRadius: 8, padding: 16, shadowColor: '#000', shadowOpacity: 0.1, shadowRadius: 4 }}>
        <View>
          <Text style={{ fontSize: 20, fontWeight: 'bold', marginBottom: 8 }}>Feedback</Text>
          <Text><Text style={{ fontWeight: 'bold' }}>Tone Analysis:</Text> Try speaking with more confidence and louder voice modulation.</Text>
          <Text><Text style={{ fontWeight: 'bold' }}>Body Language Tips:</Text> Maintain eye contact and reduce fidgeting.</Text>
          <Text style={{ fontSize: 12, color: '#6b7280', marginTop: 8 }}>*This is simulated feedback. ML model training under development.</Text>
        </View>
      </View>
    </div>
  );
};

// export default PracticeScreen; // Removed to avoid multiple default exports
const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  button: {
    backgroundColor: '#0a84ff',
    paddingVertical: 15,
    paddingHorizontal: 25,
    borderRadius: 10,
    marginVertical: 20,
  },
  buttonText: { color: '#fff', fontSize: 16 },
});
