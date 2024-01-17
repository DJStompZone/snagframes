import argparse
import io
import json
import os
import re
from typing import Any, Callable

from ffmpeg import FFmpeg  # type: ignore
from PIL import Image
from PIL.Image import Image as ImageType

IS_VALID_FR: Callable[[str], bool] = (
    lambda fr: re.match(r"^([\d\.]+(\s?\/\s?[\d\.]+)?)$", str(fr)) is not None
)


class VideoProcessor:
    def __init__(self, video_path: str):
        self.video_path: str = video_path
        super().__init__()

    def get_video_info(self) -> dict[str, Any]:
        try:
            ffprobe: FFmpeg = FFmpeg(executable="ffprobe").input(  # type: ignore
                self.video_path, print_format="json", show_streams=None
            )
            media_info_json = ffprobe.execute()
            media_info = json.loads(media_info_json)

            video_info: dict[str, Any] = next(
                stream
                for stream in media_info["streams"]
                if stream["codec_type"] == "video"
            )
            return video_info
        except Exception as e:
            print(f"An error occurred while probing the video: {e}")
            return dict({})

    def extract_frames(self, second: int | float, out_dir: str) -> None:
        video_info: dict[str, Any] = self.get_video_info()
        if not len(video_info.values()):
            return
        frame_rate: str = str(video_info.get("r_frame_rate"))
        try:
            if not IS_VALID_FR(frame_rate):
                raise ValueError(f"Invalid frame rate: {frame_rate}")
            frame_rate_n: float = float(eval(frame_rate))
        except Exception as e:
            print(f"An error occurred while parsing the frame rate ({frame_rate}): {e}")
            return

        frame_numbers = [
            int(second * frame_rate_n) + i for i in range(int(frame_rate_n))
        ]

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        for _, frame_number in enumerate(frame_numbers):
            print("Extracting frame: ", frame_number, "... ", end="", flush=True)
            frame: ImageType = self.extract_frame_by_number(frame_number)
            print("Done.")
            dest: str = os.path.join(out_dir, f"frame_{frame_number}.png")
            if os.path.exists(dest):
                print(
                    f"Frame {frame_number} already exists in destination directory. Skipping..."
                )
                continue
            print(f"Saving frame {frame_number} to: {dest} ... ", end="", flush=True)
            frame.save(dest)
            print("Done.")

    def extract_frame_by_number(self, frame_number: int) -> ImageType:
        ffmpeg_command = (
            FFmpeg()
            .input(self.video_path)  # type: ignore
            .output(
                "pipe:1",
                **{
                    "vframes": 1,
                    "f": "image2",
                    "vcodec": "png",
                    "vf": f"select=eq(n\\,{frame_number})",  # type: ignore
                    "vsync": 0,
                },
            )
        )
        stdio: bytes = ffmpeg_command.execute()
        image: ImageType = Image.open(io.BytesIO(stdio))
        return image


def main():
    parser = argparse.ArgumentParser(description="Extract frames from a video file.")
    parser.add_argument("--video", required=True, help="Path to the video file.")
    parser.add_argument(
        "--time",
        type=float,
        required=True,
        help="Time in seconds to extract frames from.",
    )
    parser.add_argument(
        "--out-dir", required=True, help="Directory to save the extracted frames."
    )
    args: argparse.Namespace = parser.parse_args()
    processor = VideoProcessor(args.video)
    _ = processor.extract_frames(args.time, args.out_dir)


if __name__ == "__main__":
    main()
