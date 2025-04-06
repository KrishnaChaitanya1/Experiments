import os
import ffmpeg

INPUT_PATH = "D:\To Export\Videos"

def skip_folders(directory):
    return [
        file for file in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, file))
    ]

video_list = skip_folders(INPUT_PATH)

for videos in video_list:
    if ".mp4" in videos:
        pass
    elif ".mkv" in videos:
        pass
    else:
        mpeg = (
            ffmpeg.input(f"{INPUT_PATH}\{videos}")
            .output(
                f"{INPUT_PATH}\{videos.replace(".webm", ".mp4")}", 
                **{"codec": "copy"}
            )
            .run()
        )
