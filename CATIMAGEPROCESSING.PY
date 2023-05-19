import tensorflow as tf
import numpy as np
import urllib
from PIL import Image

# Load the pre-trained model
model = tf.keras.applications.resnet50.ResNet50(weights='imagenet')

# Define the function to preprocess the image
def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))  # Resize the image to match the input size of the model
    image = np.array(image)  # Convert the image to a numpy array
    image = tf.keras.applications.resnet50.preprocess_input(image)  # Preprocess the image
    image = np.expand_dims(image, axis=0)  # Add a batch dimension
    return image

# Define the function to decode the predictions
def decode_predictions(preds, top=5):
    results = tf.keras.applications.resnet50.decode_predictions(preds, top=top)[0]
    return [(class_name, description, probability) for (class_name, description, probability) in results]

# Provide the URL of the cat image you want to classify
image_url = 'https://example.com/cat.jpg'

# Download the image from the provided URL
urllib.request.urlretrieve(image_url, 'cat.jpg')

# Preprocess the image
image = preprocess_image('cat.jpg')

# Make predictions
predictions = model.predict(image)

# Decode the predictions
decoded_predictions = decode_predictions(predictions, top=1)

# Print the top prediction
top_prediction = decoded_predictions[0]
print("Prediction:", top_prediction[1])
print("Probability:", top_prediction[2])
