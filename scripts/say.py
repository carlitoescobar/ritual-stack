#!/usr/bin/env python3

import sys
import os
import tempfile
from pydub import AudioSegment
from pydub.playback import play
from piper import PiperVoice

def say(text):
    """
    Convert text to speech using piper.
    """
    try:
        # Get the path to the voice model
        voice_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "piper-voices", "en_US-lessac-medium.onnx")
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "piper-voices", "en_US-lessac-medium.onnx.json")
        
        # Initialize the voice
        voice = PiperVoice.load(voice_path, config_path)
        
        # Create a temporary WAV file
        temp_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
        temp_file.close()
        
        # Synthesize speech to the temporary file
        with open(temp_file.name, 'wb') as f:
            voice.synthesize(text, f)
        
        # Load and play the audio
        audio = AudioSegment.from_wav(temp_file.name)
        play(audio)
        
        # Clean up the temporary file
        os.unlink(temp_file.name)
            
    except Exception as e:
        print(f"Error in text-to-speech: {str(e)}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        say(" ".join(sys.argv[1:]))
    else:
        print("Usage: say.py <text>", file=sys.stderr)
        sys.exit(1) 