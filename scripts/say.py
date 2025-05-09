#!/usr/bin/env python3

import sys
import os
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 say.py <text>")
        sys.exit(1)

    text = " ".join(sys.argv[1:])
    
    try:
        # Use espeak for text-to-speech
        subprocess.run(['espeak', '-v', 'en-us', '-s', '150', text], check=True)
    except Exception as e:
        print(f"Error in text-to-speech: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 