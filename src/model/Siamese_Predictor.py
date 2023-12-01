# from Siamese_Network import preprocess_image
import tensorflow as tf
from tensorflow.keras.applications import resnet
import argparse
from tensorflow.keras import metrics


def preprocess_image(filename):
    """
    Load the specified file as a JPEG image, preprocess it and
    resize it to the target shape.
    """
    target_shape = (200, 200)

    image_string = tf.io.read_file(filename)
    image = tf.image.decode_jpeg(image_string, channels=3)
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.image.resize(image, target_shape)
    return image


# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument(
    "--filename", type=str, help="Path to the input image file (e.g., img.jpg)"
)

args = parser.parse_args()

# load the model
embedding = tf.keras.models.load_model("siamese_feature.h5")


david_1 = preprocess_image(args.filename)
david_2 = preprocess_image("david_base.jpg")
# add a dimension to the tensor
david_1 = tf.expand_dims(david_1, axis=0)
david_2 = tf.expand_dims(david_2, axis=0)

anchor_embedding, positive_embedding = (
    embedding(resnet.preprocess_input(david_1)),
    embedding(resnet.preprocess_input(david_2)),
)

cosine_similarity = metrics.CosineSimilarity()

positive_similarity = cosine_similarity(anchor_embedding, positive_embedding)
print("Similarity score: ", positive_similarity.numpy())
