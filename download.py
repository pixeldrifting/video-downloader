import yt_dlp

url = input("Cole a URL do vídeo: ")
modo = input("Digite 'a' para áudio ou 'v' para vídeo: ").lower()

if modo == "a":
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
else:
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',
    }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
