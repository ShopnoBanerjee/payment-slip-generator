from flask import Flask, request, render_template, send_from_directory
from func import generate_pdf
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'inputs'
OUTPUT_FOLDER = 'static/outputs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        pdf_path = generate_pdf(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f'<a href="{pdf_path}">Download PDF</a>'

@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
