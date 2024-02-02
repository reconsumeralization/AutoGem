2. Configure Google Cloud authentication:
   ```
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
   ```
3. Set up `config.json` or environment variables with your API key:
   ```json
   {
     "API_KEY": "your_api_key_here"
   }
   ```

## Usage Examples

### Initializing the Client
```python
from src.gemini_client import GeminiClient

client = GeminiClient()
```

### Making Prediction Requests
```python
# Predict with Gemini Pro Models
results = client.predict_with_gemini_pro_models('model_name', 'path/to/image.jpg')

# Predict with Gemini Vision Pro Models
results = client.predict_with_gemini_vision_pro_models('model_name', 'path/to/image.jpg')
```

### Interpreting the Results
```python
for result in results:
    print(f"Category: {result['category']}, Confidence: {result['confidence']}, Bounding Box: {result['bounding_box']}")
```

### Configuration and Logging
```python
from src.config import Config
from src.logger import get_logger

config = Config()
api_key = config.get_api_key()

logger = get_logger('application')
logger.info("Application started")
