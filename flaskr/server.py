# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from PIL import Image, UnidentifiedImageError
import numpy as np
import cv2

app = Flask(__name__)

# Set up SQLite database


# Set up SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Image
class ImageModel(db.Model):
    __tablename__ = 'Image'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    filename = db.Column(db.String(255), nullable=False, unique=True)

# Create database tables
with app.app_context():
    db.create_all()


# Route to upload an image
@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files['image'].read()
    
    nparr = np.frombuffer(image, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # image = request.files['d']
    
    ##Save image to a folder (create the folder if it doesn't exist)
    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)
    filename = os.path.join(upload_folder, str(datetime.now()) + '.jpg')
    cv2.imwrite(filename, frame)

     
    # image.save(filename)

    # Save image information to the database using the ORM
    new_image = ImageModel(filename=filename)
    db.session.add(new_image)
    db.session.commit()

    return jsonify({'message': 'Image uploaded successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



































# # Model for Image
# class ImageModel(db.Model):
#     __tablename__ = 'Image'
#     id = db.Column(db.Integer, primary_key=True)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)
#     filename = db.Column(db.String(255), nullable=False, unique=True)

# # Create database tables
# with app.app_context():
#     db.create_all()

# @app.route('/upload', methods=['POST'])
# def upload_image():
#     # if 'image' not in request.files:
#     #     return jsonify({'error': 'No image provided'}), 400

#     # image_file = request.files['image']
    
#     # print(request.files)
    
#     # if image_file.filename == '':
#     #     return jsonify({'error': 'No image selected'}), 400
    
#     arr = request.data


#     try:
#         # Attempt to open the image using PIL
#         # image = Image.frombytes(data=arr, size=(500, 500), mode="rgb")
#         image = Image.open(BytesIO(arr))

#         # print(f"Content Type: {image_file.content_type}")
#         # print(f"File Name: {image_file.filename}")
        
#         # Save image to a folder (create the folder if it doesn't exist)
#         upload_folder = 'uploads'
#         os.makedirs(upload_folder, exist_ok=True)
#         filename = os.path.join(upload_folder, str(datetime.now()) + '.jpg')
#         image.save(filename)

#         # Save image information to the database using the ORM
#         new_image = ImageModel(filename=filename)
#         db.session.add(new_image)
#         db.session.commit()

#         return jsonify({'message': 'Image uploaded successfully'})

#     except UnidentifiedImageError:
#         # If PIL cannot identify the image, return an error response
#         return jsonify({'error': 'Invalid image file'}), 400



    
    
    
