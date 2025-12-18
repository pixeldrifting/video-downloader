import yt_dlp

url = input("Cole a URL do vídeo: ")

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'merge_output_format': 'mp4',
    'outtmpl': '%(title)s.%(ext)s',
    'noplaylist': True,
    'quiet': False,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
