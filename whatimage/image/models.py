from django.db import models
from keras.preprocessing.image import load_img, img_to_array
import os
import numpy as np
import tensorflow as tf
from keras.applications.inception_resnet_v2 import (
    InceptionResNetV2,
    decode_predictions,
    preprocess_input,
)

# Create your models here.


class Image(models.Model):
    picture = models.ImageField()
    classified = models.CharField(max_length=200, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Image classfied at {}".format(
            self.uploaded.strftime("%Y-%m-%d %H:%M:%S")
        )

    def save(self, *args, **kwargs):
        file_path = self.picture.path
        try:
            file_path = file_path.replace(" ", "_")
            img = load_img(file_path, target_size=(299, 299))
            img_arry = img_to_array(img)
            to_pred = np.expand_dims(img_arry, axis=0)
            prep = preprocess_input(to_pred)
            model = InceptionResNetV2(weights="imagenet")
            predictions = model.predict(prep)
            decoded = decode_predictions(predictions)[0][0][1]
            self.classified = str(decoded)
            print("success")

        except Exception as e:
            print("Classification failed:", str(e))
        super().save(*args, **kwargs)
