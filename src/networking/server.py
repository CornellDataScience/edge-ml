from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'images'  # Folder where uploaded images will be saved

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No file part', 400
    
    image_file = request.files['image']

    if image_file.filename == '':
        return 'No selected file', 400

    # Save the uploaded image to the UPLOAD_FOLDER
    image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(image_path)
    
    return f'Image {image_file.filename} uploaded successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

