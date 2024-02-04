import base64
import json
import requests
from src.config import Config
from google.cloud import gemini_pro_models, gemini_vision_pro_models
from src.utils import encode_image_to_base64
from src.logger import get_logger


class GeminiClient:
    def __init__(self):
        config = Config()
        self.api_key = config.get_api_key()
        self.gemini_pro_client = gemini_pro_models.Ggemini_pro_models.GeminiProModelsServiceClient()
        self.gemini_vision_pro_client = gemini_vision_pro_models.GeminiVisionProModelsServiceClient()
        self.logger = get_logger('GeminiClient')

    def predict_with_gemini_pro_models(self, model_name, image_path):
        image_bytes = encode_image_to_base64(image_path)
        request = gemini_pro_models.PredictRequest(
            name=model_name, instances=[{"b64": image_bytes}]
        )
        try:
            response = self.gemini_pro_client.predict(request=request)
            return self.parse_prediction_results(response.predictions)
        except Exception as e:
            self.logger.error(f"Error during Gemini Pro Models prediction: {e}")
            return None

    def predict_with_gemini_vision_pro_models(self, model_name, image_path):
        image_bytes = encode_image_to_base64(image_path)
        request = gemini_vision_pro_models.PredictRequest(
            name=model_name, instances=[{"b64": image_bytes}]
        )
        try:
            response = self.gemini_vision_pro_client.predict(request=request)
            return self.parse_prediction_results(response.predictions)
        except Exception as e:
            self.logger.error(f"Error during Gemini Vision Pro Models prediction: {e}")
            return None

    def parse_prediction_results(self, predictions):
        results = []
        for prediction in predictions:
            for label in prediction['labels']:
                results.append({
                    'category': label['category'],
                    'confidence': label['confidence'],
                    'bounding_box': label.get('bounding_box', None)
                })
        return results
