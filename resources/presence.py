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
                "id": "89400257-227e-4fcb-8d2f-7408a4ec0de3",
                "name": "Wisnu",
                "nik": "352215xxxxxx0004",
                "image_profile": "https://images.unsplash.com/photo-1595152452543-e5fc28ebc2b8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwcm9maWxlLXBhZ2V8N3x8fGVufDB8fHx8&w=1000&q=80",
                "mask": 1 #wear mask
            },
            {
                "id": "92cfc1de-adfe-4580-ac06-9aa6b745a5a7",
                "name": "Felix",
                "nik": "352215xxxxxx0001",
                "image_profile": "https://images.unsplash.com/photo-1595152452543-e5fc28ebc2b8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwcm9maWxlLXBhZ2V8N3x8fGVufDB8fHx8&w=1000&q=80",
                "mask": 0 #not wear
            }
        ]
    }
    return jsonify(dummy)

@presences.route('/presence/:id')
def detail():
    dummy = {
        "status": "success",
        "results": [
            {
                "id": "89400257-227e-4fcb-8d2f-7408a4ec0de3",
                "name": "Wisnu",
                "nik": "352215xxxxxx0004",
                "image_profile": "https://test.com/photo-1595152452543-e5fc28ebc2b8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwcm9maWxlLXBhZ2V8N3x8fGVufDB8fHx8&w=1000&q=80",
                "mask": 1, #wear mask
                "image_ktp": "https://test.com/test",
                "image_face": "https://test.com/test",
                "image_mask": "https://test.com/test",
                "created_at": "2012-08-08 21:46:24.862000"
            }
        ]
    }
    return jsonify(dummy)


