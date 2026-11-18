# Free Music Downloader

A collection of tools to download free music from Bandcamp and other platforms.

## Tools Included

### free-bandcamp-downloader
Download free and name-your-price albums/tracks from Bandcamp in lossless quality.

**Installation:**
```bash
pip3 install free-bandcamp-downloader
```

**Usage:**
```bash
bcdl-free --format FLAC "https://bandcamp.com/artist/album"
```

**Available formats:**
- FLAC (lossless)
- V0MP3
- 320MP3
- AAC
- Ogg
- ALAC
- WAV
- AIFF

### yt-dlp (recommended)
Universal downloader supporting YouTube, SoundCloud, Bandcamp, and more.

**Installation:**
```bash
pip3 install yt-dlp
```

**Usage:**
```bash
# Download as lossless FLAC
yt-dlp --extract-audio --audio-format flac "URL"

# Download from Bandcamp
yt-dlp -f "bestaudio" --extract-audio --audio-format flac "BANDCAMP_URL"
```

## Usage Examples

### Download a free Bandcamp album as FLAC
```bash
bcdl-free -d ~/Music -f FLAC "https://artist.bandcamp.com/album/album-name"
```

### Download multiple tracks with yt-dlp
```bash
yt-dlp --extract-audio --audio-format flac \
  "https://youtube.com/watch?v=..." \
  "https://soundcloud.com/artist/track"
```

### Batch download from a Bandcamp label page
```bash
bcdl-free "https://label.bandcamp.com"
```

## Requirements

- Python 3.8+
- pip3
- ffmpeg (for yt-dlp audio extraction)

## Related Tools

- [gain-sync](https://github.com/MahdiBoulila/gain-sync) - Normalize downloaded audio files
