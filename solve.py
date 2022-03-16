import tensorflow as tf
import os

base_dir = './fruits-360/Training'

IMAGE_SIZE = 224
BATCH_SIZE = 64

datagen = tf.keras.preprocessing.image.ImageDataGenerator(
rescale = 1./ 255,
rotation_range = 30,
width_shift_range = 0.3,
height_shift_range = 0.3,
horizontal_flip = True,
validation_split = 0.1,
fill_mode = 'nearest')


training_generator = datagen.flow_from_directory(base_dir, target_size = (IMAGE_SIZE, IMAGE_SIZE), batch_size = BATCH_SIZE, subset = 'training')



print(training_generator.class_indices)

labels = '\n'.join(sorted(training_generator.class_indices.keys()))

with open('labels.txt', 'w') as f:
    f.write(labels)


IMG_SHAPE = (IMAGE_SIZE, IMAGE_SIZE, 3)

base_model = tf.keras.applications.MobileNetV2(input_shape = IMG_SHAPE, include_top = False, weights = 'imagenet')

base_model.trainable = False

relu
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.Conv2D(32, 3, activation = 'relu'),
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(131, activation = 'softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(),
             loss = 'categorical_crossentropy',
              metrics = ['accuracy']
             )

epochs = 10

history = model.fit(training_generator, epochs = epochs, steps_per_epoch = 200)


