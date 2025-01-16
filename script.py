from yt_dlp import YoutubeDL
from sys import argv
    
len_args = len(argv)
if len_args < 2:
    print("Usage: python script.py <Youtube URL>")
    exit(1)
url = argv[1]
try:
    save_path = './Downloads'
    # Options for yt-dlp
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/best',  # Download best video and audio and merge
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save file format
        'merge_output_format': 'mp4',  # Merge video and audio into MP4 format
    }

    # Downloading the video
    print("Downloading...")
    yt = YoutubeDL(ydl_opts)
    info = yt.extract_info(url, download=True)
    yt.download([url])
except Exception as e:
    print("An error occured:", e)
finally:
    print("Video successfully downloaded !")

