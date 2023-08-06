import pytube as pt
import os
from pathlib import Path

yt = pt.YouTube("https://www.youtube.com/watch?v=LmOWKU37btU")
audio_stream = yt.streams.filter(only_audio=True).first()
downloaded_file_path = audio_stream.download()




dir_path = Path(os.path.join(downloaded_file_path, os.pardir))
print(dir_path)

for text_file in dir_path.glob("*.mp4"):
    try:
        new_file_path = text_file.rename(text_file.with_suffix(".mp3"))
    except FileExistsError:
        print(f"Error: '{text_file.with_suffix('.mp3').name}' already exists.")
    

