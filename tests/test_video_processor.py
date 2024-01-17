from snagframes.video_processor import VideoProcessor
import pytest

@pytest.fixture
def video_processor():
    return VideoProcessor('test_video.mp4')

def test_get_video_info(video_processor):
    video_info = video_processor.get_video_info()
    assert video_info is not None
    assert 'r_frame_rate' in video_info

def test_extract_frames(video_processor):
    frames = video_processor.extract_frames(1)
    assert len(frames) > 0