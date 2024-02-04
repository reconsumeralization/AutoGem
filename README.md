# AutoGem
Agent Framework for Gemini Pro

## Running Tests

To run the tests for AutoGem, navigate to the root directory of the project and execute the following command:

For Python:
```
python -m unittest discover tests
```

For detailed documentation on system architecture, setup, and usage, refer to our [documentation](docs/README.md).

### Using the `GeminiClient` Class

The `GeminiClient` class provides an interface to the Google Gemini Pro Models API and Google Gemini Vision Pro Models API. Here's how you can use it:

#### Setup

Before using the `GeminiClient`, ensure you have installed the necessary dependencies:

```shell
pip install google-cloud-gemini-pro-models google-cloud-gemini-vision-pro-models
```

You must also configure your Google Cloud authentication by setting the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your service account key file:

```shell
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
```

#### Initializing the Client

To initialize the `GeminiClient`, provide your Google Cloud API key:

```python
from src.gemini_client import GeminiClient

client = GeminiClient(api_key='YOUR_API_KEY')
```

#### Making Prediction Requests

To make prediction requests, use the `predict_with_gemini_pro_models` or `predict_with_gemini_vision_pro_models` methods. Provide the model name and the path to the image you wish to classify:

```python
# Predict with Gemini Pro Models
results = client.predict_with_gemini_pro_models('model_name', 'path/to/image.jpg')

# Predict with Gemini Vision Pro Models
results = client.predict_with_gemini_vision_pro_models('model_name', 'path/to/image.jpg')
```

#### Interpreting the Results

The methods return a list of dictionaries, each representing a prediction result. Here's how to interpret these results:

```python
for result in results:
    print(f"Category: {result['category']}, Confidence: {result['confidence']}, Bounding Box: {result['bounding_box']}")
```

### Known Issues and Limitations

For detailed documentation on system architecture, setup, and usage, refer to our [documentation](docs/README.md).

- The current implementation does not support streaming predictions.
- Only prediction requests with single instances (images) are supported; batch predictions are not yet implemented.
- The API may impose limits on the number of requests per minute or other usage restrictions.
