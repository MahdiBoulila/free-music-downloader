#!/usr/bin/env python3
"""
Download free tracks from Bandcamp using yt-dlp and convert to AIFF.
"""

import subprocess
import sys
from pathlib import Path


def download_bandcamp_track(url: str, output_dir: str = ".") -> bool:
    """Download a track from Bandcamp as AIFF."""
    output = Path(output_dir) / "%(title)s.%(ext)s"
    
    cmd = [
        "yt-dlp",
        "--extract-audio",
        "--audio-format", "aiff",
        "--audio-quality", "0",
        "-o", str(output),
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


def download_bandcamp_album(url: str, output_dir: str = ".") -> bool:
    """Download an album from Bandcamp as AIFF."""
    output = Path(output_dir) / "%(playlist_title)s/%(title)s.%(ext)s"
    
    cmd = [
        "yt-dlp",
        "--extract-audio",
        "--audio-format", "aiff",
        "--audio-quality", "0",
        "-o", str(output),
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
        print("Usage: python download_bandcamp_ytdlp.py <url>")
        print("Downloads as AIFF format")
        sys.exit(1)
    
    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    
    # Check if it's an album or track URL
    if "/album/" in url:
        success = download_bandcamp_album(url, output_dir)
    else:
        success = download_bandcamp_track(url, output_dir)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
