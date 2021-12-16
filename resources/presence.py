from flask import Blueprint, request, jsonify

from services.generate_img import GenerateImage
from services.mask_detection import MaskDetection

presences = Blueprint('presences', __name__)

@presences.route('/')
def index():
    return 'Hello World!'

@presences.route('/img', methods=['POST'])
def process_image():
    file = request.form['image']
    cv_image = GenerateImage.decodeImageToCV(file)
    result = MaskDetection.classifyImage(cv_image)
    return jsonify({'status': 'success', 'msg': f'Result: {result}'})

@presences.route('/presences')
def list():
    dummy = {
        "status": "success",
        "results": [
            {
                "name": "Wisnu",
                "nik": "352215xxxxxx0004",
                "imageUrl": "https://images.unsplash.com/photo-1595152452543-e5fc28ebc2b8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwcm9maWxlLXBhZ2V8N3x8fGVufDB8fHx8&w=1000&q=80"
            },
            {
                "name": "Felix",
                "nik": "352215xxxxxx0001",
                "imageUrl": "https://images.unsplash.com/photo-1595152452543-e5fc28ebc2b8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwcm9maWxlLXBhZ2V8N3x8fGVufDB8fHx8&w=1000&q=80"
            }
        ]
    }
    return jsonify(dummy)



