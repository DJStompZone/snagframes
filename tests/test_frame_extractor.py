from snagframes.frame_extractor import FrameExtractor
import pytest

@pytest.fixture
def frame_extractor():
    return FrameExtractor('test_video.mp4')

def test_extract(frame_extractor):
    frame = frame_extractor.extract(25, 30)
    assert frame is not None