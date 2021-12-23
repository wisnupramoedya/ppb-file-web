from datetime import datetime
from flask import Blueprint, request, jsonify, send_from_directory
from models.presence import Presence
from app import db

from services.generate_img import GenerateImage

presences = Blueprint('presences', __name__)

@presences.route('/')
def index():
    return 'Hello World!'

@presences.route('/presences')
def list():
    presences = Presence.query.all()
    results = [
        presence.as_dict() for presence in presences
    ]
    return jsonify(results)

@presences.route('/presence/<id>')
def detail(id):
    presence = Presence.query.get(id)
    results = [
        presence.as_dict()
    ]
    
    return jsonify(results)

@presences.route('/presence', methods=['POST'])
def create_presence():
    date_now = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_mask = GenerateImage.decodeBase64toImage(request.form["image_mask"], "image_mask", date_now)
    mask = GenerateImage.process_image(request.form["image_mask"])
    
    presence = Presence(
        name = request.form["name"],
        nik = request.form["nik"],
        image_mask = image_mask,
        mask = mask
    )

    db.session.add(presence)
    db.session.commit()

    return jsonify(presence.as_dict())

@presences.route("/static/<path:name>")
def download_file(name):
    return send_from_directory(
        "../static", name
    )