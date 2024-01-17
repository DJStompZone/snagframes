from PIL import Image


class FileManager:
    @staticmethod
    def save_frame(frame: Image.Image, output_path: str):
        try:
            frame.save(output_path)
        except IOError as e:
            print(f"An error occurred while saving the frame: {e}")
