from os import stat
from PIL import Image
from io import BytesIO
import base64
import numpy as np
import cv2

class GenerateImage:
    DIM = (224, 224)

    @staticmethod
    def decodeImageToCV(base_file):
        image = base64.b64decode(base_file)
        arr_image = np.array(Image.open(BytesIO(image)).convert('RGB'))

        cv_image = arr_image[:, :, ::-1].copy()
        cv_image = cv2.resize(cv_image, dsize=GenerateImage.DIM)

        return cv_image

    