#!/usr/bin/env python3
"""
Simple Bandcamp downloader using free-bandcamp-downloader.
"""

import subprocess
import sys
from pathlib import Path


def download_bandcamp_track(url: str, format: str = "FLAC") -> bool:
    """Download a track from Bandcamp."""
    cmd = [
        "bcdl-free",
        "-f", format,
        "--no-unzip",
        url
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✓ Downloaded: {url}")
        return True
    else:
        print(f"✗ Failed: {url}")
        print(result.stderr)
        return False


def download_bandcamp_album(url: str, format: str = "FLAC") -> bool:
    """Download an album from Bandcamp."""
    cmd = [
        "bcdl-free",
        "-f", format,
        url
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✓ Downloaded album: {url}")
        return True
    else:
        print(f"✗ Failed album: {url}")
        print(result.stderr)
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python download_bandcamp.py <url> [format]")
        print("Formats: FLAC, V0MP3, 320MP3, AAC, Ogg, ALAC, WAV, AIFF")
        sys.exit(1)
    
    url = sys.argv[1]
    format = sys.argv[2] if len(sys.argv) > 2 else "FLAC"
    
    # Check if it's an album or track URL
    if "/album/" in url:
        success = download_bandcamp_album(url, format)
    else:
        success = download_bandcamp_track(url, format)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
