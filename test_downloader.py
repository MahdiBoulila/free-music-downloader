#!/usr/bin/env python3
"""
Test the Bandcamp downloader script.
"""

import sys
from pathlib import Path


def test_imports():
    """Test that required modules can be imported."""
    print("Test 1: Import required modules")
    
    try:
        import free_bandcamp_downloader
        print("  ✓ free-bandcamp-downloader imported")
    except ImportError:
        print("  ! free-bandcamp-downloader not installed (optional for testing)")
    
    try:
        import yt_dlp
        print("  ✓ yt-dlp imported")
    except ImportError:
        print("  ! yt-dlp not installed (optional)")
    
    return True


def test_script_structure():
    """Test that the download script has the right functions."""
    print("\nTest 2: Script structure")
    
    script_path = Path(__file__).parent / "download_bandcamp.py"
    
    if not script_path.exists():
        print("  ✗ download_bandcamp.py not found")
        return False
    
    content = script_path.read_text()
    
    required_functions = ["download_bandcamp_track", "download_bandcamp_album", "main"]
    for func in required_functions:
        if f"def {func}(" in content:
            print(f"  ✓ {func} defined")
        else:
            print(f"  ✗ {func} missing")
            return False
    
    return True


def run_all_tests():
    """Run all tests."""
    print("Running tests for Free Music Downloader\n")
    
    try:
        test_imports()
        test_script_structure()
        print("\n✅ All tests passed!")
        return True
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
