from Siamese_Network import SiameseNetwork
from tensorflow.keras.optimizers import Adam
from data_loader import DataLoader

import os

WIDTH = HEIGHT = 105
CEELS = 1
seed = 0
loss_type = "binary_crossentropy"

data_path = "realtime"

train_path = os.path.join(data_path, "train.pickle")  # A path for the train file

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

loader = DataLoader(
    width=WIDTH,
    height=HEIGHT,
    cells=CEELS,
    data_path=data_path,
    output_path=train_path,
)
loader.load(set_name="train")

siamese.fit(
    weights_file="weights/weights.h5",
    train_path=train_path,
    validation_size=0.2,
    batch_size=32,
    epochs=2,
    early_stopping=True,
    patience=5,
    min_delta=0.1,
)
