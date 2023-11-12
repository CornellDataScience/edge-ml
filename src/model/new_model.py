import cv2
import os
import numpy as np
from keras.preprocessing import image
from keras.models import load_model
from sklearn.metrics.pairwise import cosine_similarity


# Load the pre-trained FaceNet model
model = load_model('faces.h5')


def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))  # Resize to model's input size
    img = img.astype('float32')  # Convert to float
    mean, std = img.mean(), img.std()
    img = (img - mean) / std  # Normalize
    return np.expand_dims(img, axis=0)  # Add batch dimension


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        # Add other file types if needed
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(folder, filename)
            preprocessed_img = preprocess_image(img_path)
            images.append(preprocessed_img)
    return images


# Load and preprocess all images in the folder
folder_path = 'train'
preprocessed_images = load_images_from_folder(folder_path)


def get_embedding(model, face_pixels):
    # Get the embedding
    embedding = model.predict(face_pixels)
    return embedding[0]

# embeddings = [get_embedding(model, img) for img in preprocessed_images]


# Load and preprocess images
image1 = preprocess_image('train/will-smith_cropped_2.jpg')
image2 = preprocess_image('train/will-smith_cropped_3.jpg')

# Get embeddings
embedding1 = get_embedding(model, image1)
embedding2 = get_embedding(model, image2)

# Calculate similarity (e.g., using cosine similarity)
similarity = cosine_similarity([embedding1], [embedding2])
print(similarity)
