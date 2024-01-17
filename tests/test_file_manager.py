from snagframes.file_manager import FileManager
from PIL import Image
import pytest
import os

def test_save_frame():
    frame = Image.new('RGB', (100, 100), color = 'red')
    output_path = 'test_frame.jpg'
    FileManager.save_frame(frame, output_path)
    assert os.path.exists(output_path)
    os.remove(output_path)