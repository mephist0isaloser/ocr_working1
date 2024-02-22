from flask import Flask, request, jsonify, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = r"C:\Users\mohit\PycharmProjects\flaskProject\image_sauce"

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('upload.html')  # Render upload.html instead of displaying text

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json
    result = {'message': 'Data processed successfully', 'data': data}
    return jsonify(result)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    return render_template('upload.html')  # Render upload.html with the form

if __name__ == '__main__':
    app.run(debug=True)
