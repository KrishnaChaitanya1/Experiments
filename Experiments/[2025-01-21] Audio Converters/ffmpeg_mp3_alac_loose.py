import os
import ffmpeg

INPUT_PATH = "D:\To Export\Music"

music_list = os.listdir(INPUT_PATH)

for music in music_list:
    mpeg = (
        ffmpeg.input(f"{INPUT_PATH}\{music}")
        .output(
            f"{INPUT_PATH}\{music.replace(".mp3", ".m4a")}", 
            **{
                "vcodec": "copy",
                "acodec": "alac"
            }
        )
        .run()
    )
