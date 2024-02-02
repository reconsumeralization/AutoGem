import base64
import json

from src import config_manager

import requests
from google.cloud import gemini_pro_models, gemini_vision_pro_models
from src import logger
from src.utils import encode_image_to_base64


class GeminiClient:
    def __init__(self):
        self.api_key = config_manager.get_config_value("API_KEY")
        self.gemini_pro_client = gemini_pro_models.Ggemini_pro_models.GeminiProModelsServiceClient()
        self.gemini_vision_pro_client = gemini_vision_pro_models.GeminiVisionProModelsServiceClient()

    def predict_with_gemini_pro_models(self, model_name, image_path):
        image_bytes = encode_image_to_base64(image_path)
        request = gemini_pro_models.PredictRequest(
            name=model_name, instances=[{"b64": image_bytes}]
        )
        try:
            response = self.gemini_pro_client.predict(request=request)
            return self.parse_prediction_results(response.predictions)
        except Exception as e:
            logger.error(f"Error during Gemini Pro Models prediction: {e}")
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
            logger.error(f"Error during Gemini Vision Pro Models prediction: {e}")
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
