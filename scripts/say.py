#!/usr/bin/env python3

import sys
import os
import tempfile
import pygame
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
        
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Load and play the audio
        pygame.mixer.music.load(temp_file.name)
        pygame.mixer.music.play()
        
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        # Clean up pygame
        pygame.mixer.quit()
        
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