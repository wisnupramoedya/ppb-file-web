import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from mtcnn import MTCNN
import cv2

class MaskDetection:
    @staticmethod
    def classifyImage(image):
        detector = MTCNN()
        faces = detector.detect_faces(image)

        for result in faces:
            x, y, w, h = result['box']
            x1, y1 = x + w, y + h

            face = image[y:y1, x:x1]
            # face = cv2.cvtColor(face, cv2.COLOR_BGR2)
            face = cv2.resize(face, (224, 224))
            face = img_to_array(face)
            face = preprocess_input(face)
            face = np.expand_dims(face, axis=0)
            break

        interpreter = tf.lite.Interpreter(model_path='mask_model.tflite')
        interpreter.allocate_tensors()

        # Get input and output tensors.
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        # Test model on random input data.
        input_shape = input_details[0]['shape']
        interpreter.set_tensor(input_details[0]['index'], face)
        interpreter.invoke()

        # The function `get_tensor()` returns a copy of the tensor data.
        # Use `tensor()` in order to get a pointer to the tensor.
        output_data = interpreter.get_tensor(output_details[0]['index'])
        return MaskDetection.check_index(output_data)
    
    @staticmethod
    def check_index(output_data):
        with_mask = output_data[0][0]
        without_mask = output_data[0][1]

        print(f"{with_mask} and {without_mask} so {'No mask' if with_mask < without_mask else 'Mask'}")
        return 0 if with_mask < without_mask else 1