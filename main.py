from flask import Flask, request, jsonify
import os
from PIL import Image
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

app = Flask(__name__)

# Load the pre-trained semaphore model
model_path = 'model_ml.h5'
model = load_model(model_path)

# Semaphore classes
classes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']


# Function to preprocess the image
def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((150, 150))  # Adjust the size to match the expected input size of the model
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img


# Route for semaphore image classification
@app.route('/classify_semaphore', methods=['POST'])
def classify_semaphore():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']

    # Save the uploaded image temporarily
    temp_image_path = 'temp_image.jpg'
    image_file.save(temp_image_path)

    # Preprocess the image
    preprocessed_image = preprocess_image(temp_image_path)

    # Perform prediction
    predictions = model.predict(preprocessed_image)

    # Get the class with the highest probability
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = classes[predicted_class_index]

    # Get the confidence of the prediction
    confidence = float(predictions[0][predicted_class_index])

    # Set a threshold for confidence (adjust as needed)
    confidence_threshold = 0.5  # Example threshold value

    # Prepare JSON response
    if confidence >= confidence_threshold:
        response = {
            'predicted_class': predicted_class,
            'confidence': confidence
        }
    else:
        response = {
            'predicted_class': 'Not a Semaphore',
            'confidence': confidence
        }

    # Remove the temporary image file
    os.remove(temp_image_path)

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)