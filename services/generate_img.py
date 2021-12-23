from flask import url_for
from PIL import Image
from io import BytesIO
import base64
import numpy as np
import cv2

from services.mask_detection import MaskDetection

class GenerateImage:
    DIM = (224, 224)
    STATIC_FOLDER = 'static/'

    @staticmethod
    def decodeImageToCV(base_file):
        image = base64.b64decode(base_file)
        arr_image = np.array(Image.open(BytesIO(image)).convert('RGB'))

        cv_image = arr_image[:, :, ::-1].copy()
        cv_image = cv2.resize(cv_image, dsize=GenerateImage.DIM)

        return cv_image

    @staticmethod
    def decodeBase64toImage(base_string, prefix, id):
        filename = "image/{}_{}.png".format(prefix, id)
        with open(GenerateImage.STATIC_FOLDER + filename, "wb") as fh:
            fh.write(base64.b64decode(base_string))
        
        return GenerateImage.STATIC_FOLDER + filename

    @staticmethod
    def process_image(file):
        cv_image = GenerateImage.decodeImageToCV(file)
        return MaskDetection.classifyImage(cv_image)
    