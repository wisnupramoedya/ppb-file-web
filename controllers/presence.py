from datetime import datetime
from flask import Blueprint, request, jsonify, send_from_directory
from models.presence import Presence
from app import db

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
    presences = Presence.query.all()
    results = {
        "results": [
            presence.as_dict() for presence in presences
        ]
    }
    return jsonify(results)

@presences.route('/presence/<id>')
def detail(id):
    presence = Presence.query.get(id)
    results = {
        "results": [
            presence.as_dict()
        ]
    }
    return jsonify(results)

@presences.route('/presence', methods=['POST'])
def create_presence():
    date_now = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_profile = GenerateImage.decodeBase64toImage(request.form["image_profile"], "image_profile", date_now)
    image_ktp = GenerateImage.decodeBase64toImage(request.form["image_ktp"], "image_ktp", date_now)
    image_face = GenerateImage.decodeBase64toImage(request.form["image_face"], "image_face", date_now)
    image_mask = GenerateImage.decodeBase64toImage(request.form["image_mask"], "image_mask", date_now)
    
    presence = Presence(
        name = request.form["name"],
        nik = request.form["nik"],
        image_profile = image_profile,
        image_ktp = image_ktp,
        image_face = image_face,
        image_mask = image_mask,
        mask = 1
    )

    db.session.add(presence)
    db.session.commit()

    return jsonify(presence.as_dict())

@presences.route("/static/<path:name>")
def download_file(name):
    return send_from_directory(
        "../static", name
    )