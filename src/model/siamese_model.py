from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.layers import MaxPooling2D

img_rows, img_cols = 224, 224
print(img_rows, img_cols)


def create_model():
    inputs = Input((img_rows, img_cols, 3))
    x = Conv2D(96, (11, 11), padding="same", activation="relu")(inputs)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = Dropout(0.3)(x)

    x = Conv2D(256, (5, 5), padding="same", activation="relu")(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = Dropout(0.3)(x)

    x = Conv2D(384, (3, 3), padding="same", activation="relu")(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = Dropout(0.3)(x)

    pooledOutput = GlobalAveragePooling2D()(x)
    pooledOutput = Dense(1024)(pooledOutput)
    outputs = Dense(128)(pooledOutput)

    model = Model(inputs, outputs)
    return model


from tensorflow.keras.layers import Lambda
from tensorflow.keras import backend as K

feature_extractor = create_model()
imgA = Input(shape=(img_rows, img_cols, 3))
imgB = Input(shape=(img_rows, img_cols, 3))
featA = feature_extractor(imgA)
featB = feature_extractor(imgB)

print("checkpoint 1")


def euclidean_distance(vectors):
    (featA, featB) = vectors
    sum_squared = K.sum(K.square(featA - featB), axis=1, keepdims=True)
    return K.sqrt(K.maximum(sum_squared, K.epsilon()))


distance = Lambda(euclidean_distance)([featA, featB])
outputs = Dense(1, activation="sigmoid")(distance)
model = Model(inputs=[imgA, imgB], outputs=outputs)

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

import numpy as np

print("checkpoint 2")


def generate_train_image_pairs(images_dataset, labels_dataset):
    unique_labels = np.unique(labels_dataset)
    label_wise_indices = dict()
    for label in unique_labels:
        label_wise_indices.setdefault(
            label,
            [
                index
                for index, curr_label in enumerate(labels_dataset)
                if label == curr_label
            ],
        )

    pair_images = []
    pair_labels = []
    for index, image in enumerate(images_dataset):
        pos_indices = label_wise_indices.get(labels_dataset[index])
        pos_image = images_dataset[np.random.choice(pos_indices)]
        pair_images.append((image, pos_image))
        pair_labels.append(1)

        neg_indices = np.where(labels_dataset != labels_dataset[index])
        neg_image = images_dataset[np.random.choice(neg_indices[0])]
        pair_images.append((image, neg_image))
        pair_labels.append(0)
    return np.array(pair_images), np.array(pair_labels)


import glob
import cv2
from tensorflow.keras.utils import img_to_array

# pull images from david/ folder
images_dataset = []
labels_dataset = []
images_test_dataset = []
labels_test_dataset = []

for image_path in glob.glob("david/david*.jpg"):
    image = cv2.imread(image_path)
    # print(image.shape)
    # need to bounding box here
    image = cv2.resize(image, (img_rows, img_cols))
    image = img_to_array(image)
    images_dataset.append(image)
    label = "david"
    labels_dataset.append(label)

for image_path in glob.glob("david/test*.jpg"):
    image = cv2.imread(image_path)
    print(image.shape, image_path)
    # need to bounding box here
    image = cv2.resize(image, (img_rows, img_cols))
    image = img_to_array(image)
    images_test_dataset.append(image)
    label = "david" if "test_david" in image_path else "other"
    labels_test_dataset.append(label)

## Model training

images_pair, labels_pair = generate_train_image_pairs(images_dataset, labels_dataset)
history = model.fit(
    [images_pair[:, 0], images_pair[:, 1]],
    labels_pair[:],
    validation_split=0.1,
    batch_size=64,
    epochs=5,
)

print("checkpoint 3")


def generate_test_image_pairs(images_dataset, labels_dataset, image):
    unique_labels = np.unique(labels_dataset)
    label_wise_indices = dict()
    for label in unique_labels:
        label_wise_indices.setdefault(
            label,
            [
                index
                for index, curr_label in enumerate(labels_dataset)
                if label == curr_label
            ],
        )

    pair_images = []
    pair_labels = []
    for label, indices_for_label in label_wise_indices.items():
        test_image = images_dataset[np.random.choice(indices_for_label)]
        pair_images.append((image, test_image))
        pair_labels.append(label)
    return np.array(pair_images), np.array(pair_labels)


def predict(image):
    test_image_pairs, test_label_pairs = generate_test_image_pairs(
        images_dataset, labels_dataset, image
    )  # produce an array of test image pairs and test label pairs
    # print("Test pairs", test_image_pairs)
    print("Test labels", test_label_pairs)
    for index, pair in enumerate(test_image_pairs):
        pair_image1 = np.expand_dims(pair[0], axis=-1)
        pair_image1 = np.expand_dims(pair_image1, axis=0)
        pair_image2 = np.expand_dims(pair[1], axis=-1)
        pair_image2 = np.expand_dims(pair_image2, axis=0)
        prediction = model.predict([pair_image1, pair_image2])[0][0]
        print("Test image pair {} similarity: {:.2f}".format(index, prediction))


print(labels_test_dataset)

# show the first image
predict(images_test_dataset[0])

predict(images_test_dataset[1])
