# from Siamese_Network import preprocess_image
import tensorflow as tf
from tensorflow.keras.applications import resnet
import argparse
from tensorflow.keras import metrics
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import threading

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

# load the model
embedding = tf.keras.models.load_model("siamese_feature.h5", compile=False)
print("Model is done loading")

# load david base
david_2 = preprocess_image("david_base.jpg")
david_2 = tf.expand_dims(david_2, axis=0)

def get_similarity_score(img_path):
    time.sleep(0.5);
    david_1 = preprocess_image(img_path)
    
    # add a dimension to the tensor
    david_1 = tf.expand_dims(david_1, axis=0)
    
    # get embeddings
    anchor_embedding, positive_embedding = (
        embedding(resnet.preprocess_input(david_1)),
        embedding(resnet.preprocess_input(david_2)),
    )
    
    # get similarity score
    cosine_similarity = metrics.CosineSimilarity()

    positive_similarity = cosine_similarity(anchor_embedding, positive_embedding)
    print(f"Similarity score for {img_path}: ", positive_similarity.numpy())

# set up on created
def on_created(event):
    print(f"hey, {event.src_path} has been created!")
    model_thread = threading.Thread(target=lambda: get_similarity_score(event.src_path))
    model_thread.start()

# set up watchdog
patterns = ["*"]
ignore_patterns = None
ignore_directories = False
case_sensitive = True
my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
my_event_handler.on_created = on_created

# create observer
path = "../../Images/bounding_boxes"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

# run observer
my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
