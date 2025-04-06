import os
import argparse
import ffmpeg

parser = argparse.ArgumentParser()
parser.add_argument("input_path")
input_path = parser.parse_args().input_path

music_list = os.listdir(input_path)

for music in music_list:
    mpeg = (
        ffmpeg.input(f"{input_path}\{music}")
        .output(
            f"{input_path}\{music.replace(".opus", ".m4a")}", 
            **{
                "vcodec": "copy",
                "acodec": "alac"
            }
        )
        .run()
    )
