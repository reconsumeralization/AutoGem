import base64
import os
from src.logger import get_logger

def encode_image_to_base64(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The specified image file does not exist: {image_path}")
        logger = get_logger('utils')
    if not os.path.exists(image_path):
        logger.error(f"The specified image file does not exist: {image_path}")
        raise FileNotFoundError(f"The specified image file does not exist: {image_path}")
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def validate_image_file(image_path):
    logger = get_logger('utils')
    if not os.path.isfile(image_path):
        logger.error(f"Invalid image file path: {image_path}")
        raise ValueError(f"Invalid image file path: {image_path}")
    if not image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise ValueError("Unsupported image format. Please use PNG or JPEG.")
