import numpy as np
import tensorflow as tf

class MaskDetection:
    @staticmethod
    def classifyImage(image):
        input_data = np.array(image, dtype=np.float32)
        input_data = np.expand_dims(input_data, axis=0)

        interpreter = tf.lite.Interpreter(model_path='mask_model.tflite')
        interpreter.allocate_tensors()

        # Get input and output tensors.
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        # Test model on random input data.
        input_shape = input_details[0]['shape']
        interpreter.set_tensor(input_details[0]['index'], input_data)
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