import io

from ffmpeg import FFmpeg  # type: ignore
from PIL import Image


class FrameExtractor:
    def __init__(self, video_path: str) -> None:
        self.video_path = video_path
        super().__init__()

    def extract(self, exact_time: float) -> Image.Image:
        ffmpeg = (
            FFmpeg()  # type: ignore
            .input(self.video_path, ss=str(exact_time))
            .output("pipe:", vframes=1, format="image2", vcodec="png")
        )
        stdio: bytes = ffmpeg.execute()
        image = Image.open(io.BytesIO(stdio))
        return image
