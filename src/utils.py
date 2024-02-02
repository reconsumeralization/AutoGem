import base64
import os

from PIL import Image


def encode_image_to_base64(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The specified image file does not exist: {image_path}")
    with Image.open(image_path) as image:
        image_bytes = image.tobytes()
        encoded_string = base64.b64encode(image_bytes).decode('utf-8')
    return encoded_string

def validate_image_file(image_path):
    if not os.path.isfile(image_path):
        raise ValueError(f"Invalid image file path: {image_path}")
    if not image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise ValueError("Unsupported image format. Please use PNG or JPEG.")
