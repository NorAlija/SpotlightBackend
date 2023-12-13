# Image Upload Application

## Overview

This project involves the development of a Flask-based web application designed for uploading images and storing their metadata in a SQLite database. The application utilizes Flask, Flask-SQLAlchemy, and other related libraries to handle HTTP requests, manage the SQLite database, and interact with the file system. This project serves as an introduction to using these technologies.

## Application Functionality

The primary functionality of the application is to enable the model server to upload images through a designated API endpoint. The uploaded images are then stored on the server, and relevant information, such as filename and timestamp, is recorded in a SQLite database using Flask-SQLAlchemy.

## Technologies Used

- **Flask:** A micro web framework for Python used to handle web requests and responses.
- **Flask-SQLAlchemy:** An extension for Flask that simplifies the integration of SQLAlchemy, a SQL toolkit, and Object-Relational Mapping (ORM) library.
- **SQLite:** A lightweight, serverless, and self-contained SQL database engine used to store image metadata.
- **PIL (Pillow):** Python Imaging Library (Pillow), used for image processing tasks such as saving uploaded images.
- **NumPy:** A library for numerical operations, used for handling image data.
- **IO (BytesIO):** Input/output tools for handling binary data streams.

## Application Components

### 1. Flask Application Setup

- The Flask application is initialized using the Flask constructor.
- SQLite database configuration is set up to use the SQLAlchemy ORM for managing database interactions.

### 2. ImageModel Class

- Defines the data model for image information, including fields like ID, timestamp, and filename.
- This class extends the db.Model class from Flask-SQLAlchemy.

### 3. Database Initialization

- Database tables are created using the db.create_all() method within the Flask application context.

### 4. Image Upload Route

- The /upload route is configured to accept HTTP POST requests for image uploads.
- Uploaded images are saved to a designated folder (uploads) on the server.
- Image metadata (filename) is stored in the SQLite database using the Flask-SQLAlchemy ORM.

### 5. Application Execution

- The application runs on the specified host (0.0.0.0) and port (5000) in debug mode.



## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies:**
   ```bash
   pip install flask flask_sqlalchemy Pillow
   ```

## Running the Application

1. **Run the Flask Application:**
   ```bash
   flask run --app flaskr --debug

   ```
## API Endpoints

### Upload Image

- **Endpoint:**
  - `/upload`

- **Method:**
  - `POST`

- **Request Payload:**
  - Include an image file in the request payload with the key `d`.

- **Response:**
  - Upon successful upload, the server will respond with a JSON message:
    ```json
    {
      "message": "Image uploaded successfully"
    }
    ```

## Conclusion

This project introduces the basics of creating a web application using Flask and storing data in a SQLite database. It showcases the integration of Flask-SQLAlchemy for managing database interactions and includes functionality to handle image uploads. This project serves as an entry-level exploration into web development and database integration using Flask and related technologies.
