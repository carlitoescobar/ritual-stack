#!/usr/bin/env python3

import sys
import subprocess
import os

def say(text):
    """
    Convert text to speech using piper.
    """
    try:
        # Get the path to the piper executable
        piper_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "piper")
        
        # Get the path to the voice model
        voice_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "piper-voices", "en_US-lessac-medium.onnx")
        
        # Run piper with the text and voice model
        subprocess.run([piper_path, "--model", voice_path, "--output_file", "/dev/stdout"], input=text.encode(), check=True)
    except Exception as e:
        print(f"Error in text-to-speech: {str(e)}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        say(" ".join(sys.argv[1:]))
    else:
        print("Usage: say.py <text>", file=sys.stderr)
        sys.exit(1) 