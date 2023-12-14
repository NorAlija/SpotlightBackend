# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from PIL import Image, UnidentifiedImageError
import numpy as np
import cv2

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ImageModel(db.Model):
    __tablename__ = 'Image'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    filename = db.Column(db.String(255), nullable=False, unique=True)


with app.app_context():
    db.create_all()


@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files['image'].read()
    
    nparr = np.frombuffer(image, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    
    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)
    filename = os.path.join(upload_folder, str(datetime.now()) + '.jpg')
    cv2.imwrite(filename, frame)


    new_image = ImageModel(filename=filename)
    db.session.add(new_image)
    db.session.commit()

    return jsonify({'message': 'Image uploaded successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



































    
    
    
