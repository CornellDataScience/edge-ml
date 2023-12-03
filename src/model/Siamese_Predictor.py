import sklearn
import threading
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
import numpy as np
import time

from utils import preprocess_image

from tensorflow.keras.applications import resnet
from tensorflow.keras import metrics

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import threading
from Siamese_Network import SiameseNetwork
from PIL import Image


WIDTH = HEIGHT = 105
CEELS = 1
seed = 0
loss_type = "binary_crossentropy"


def preprocess_image(filename):
    """
    Load the specified file as a JPEG image, preprocess it and
    resize it to the target shape.
    """
    img = Image.open(filename)

    # resize images to 105 x 105
    img = img.resize((WIDTH, HEIGHT))
    # make black white and reduce channels to 1
    img = img.convert("L")
    img = np.array(img)
    img = img.reshape(WIDTH, HEIGHT, CEELS)
    img = img.reshape(1, WIDTH, HEIGHT, CEELS)

    return img


from message import sms_message

# load the model
siamese = SiameseNetwork(
    seed=seed,
    width=WIDTH,
    height=HEIGHT,
    cells=CEELS,
    loss=loss_type,
    metrics=["accuracy"],
    optimizer=Adam(lr=0.00005),
    dropout_rate=0.4,
)
siamese._load_weights(
    "weights/weights_seed_0_lr_5e-05_bs_32_ep_10_val_0.2_es_True_pa_5_md_0.1.h5"
)
print("Model is done loading")

# load david base
david_2 = preprocess_image("david_base.jpg")


def get_similarity_score(img_path):
    time.sleep(0.5)
    david_1 = preprocess_image(img_path)

    # add a dimension to the tensor
    # get embeddings
    prob = siamese.predict([david_2, david_1], ["David Han"])
    # positive_similarity = cosine_similarity(anchor_embedding, positive_embedding)
    # print(f"Similarity score for {img_path}: ", positive_similarity.numpy())
    print(f"Probability of David: {prob}", prob)
    threshold = 0.8
    print("Sending message")
    # sms_message.send_message(positive_similarity.numpy() < threshold)
    sms_message.send_message(prob < threshold)

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
my_event_handler = PatternMatchingEventHandler(
    patterns, ignore_patterns, ignore_directories, case_sensitive
)
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
