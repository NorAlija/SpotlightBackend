# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Set up SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Image
class Image(db.Model):
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
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({'error': 'No image selected'}), 400

    # Save image to a folder (create the folder if it doesn't exist)
    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)
    filename = os.path.join(upload_folder, str(datetime.now()) + '.jpg')
    image.save(filename)

    # Save image information to the database using the ORM
    new_image = Image(filename=filename)
    db.session.add(new_image)
    db.session.commit()

    return jsonify({'message': 'Image uploaded successfully'})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

    
    
    
# Route to upload an image
# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image provided'}), 400

#     image = request.files['image']

#     if image.filename == '':
#         return jsonify({'error': 'No image selected'}), 400

#     # Save image to a folder (create the folder if it doesn't exist)
#     upload_folder = 'uploads'
#     os.makedirs(upload_folder, exist_ok=True)
#     filename = os.path.join(upload_folder, str(datetime.now()) + '.jpg')
#     image.save(filename)

#     # Save image information to the database
#     # new_image = Image(filename=filename)
#     db.execute(
#                     "INSERT INTO Image (filename) VALUES (?, ?)",
#                     (filename),
#                 )
#     # db.session.add(new_image)
#     db.commit()

#     return jsonify({'message': 'Image uploaded successfully'})
