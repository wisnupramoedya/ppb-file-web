from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import base64
import numpy as np
import tensorflow as tf
import cv2

DIM = (224, 224)

app = Flask(__name__)

@app.route("/img", methods=["POST"])
def process_image():
    file = request.form['image']
    image = base64.b64decode(file)
    img = np.array(Image.open(BytesIO(image)).convert('RGB'))
    open_cv = img[:, :, ::-1].copy()
    open_cv = cv2.resize(open_cv, dsize=DIM)
    return jsonify({'status': 'success', 'msg': f'Result: {classifyImage(open_cv)}'})

@app.route("/")
def index():
    return "Hello World!"

def classifyImage(img):
    input_data = np.array(img, dtype=np.float32)
    input_data = np.expand_dims(input_data, axis=0)

    interpreter = tf.lite.Interpreter(model_path="mask_model.tflite")
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
    return check_index(output_data)

def check_index(output_data):
    with_mask = output_data[0][0]
    without_mask = output_data[0][1]
    print(f'{with_mask} and {without_mask}')
    return "No mask" if with_mask < without_mask else "Mask"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)