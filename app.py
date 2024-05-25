from flask import Flask, request, render_template, send_from_directory,url_for
from func import generate_pdf
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'input'
OUTPUT_FOLDER = './'
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
        filename = filename.replace(".xlsx",'')
        print(filename)
        pdf = generate_pdf(filename)
        return render_template('download.html',pdf=pdf)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(".//",filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)


