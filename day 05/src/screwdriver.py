import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'ogg'}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)


@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))
    else:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return render_template('index.html', files=files, message='Non-audio file detected')


@app.route('/uploads/<filename>')
def play_file(filename):
    if allowed_file(filename):
        template_context = dict(filename=filename, file_path=url_for(
            'static', filename=f'uploads/{filename}'))
        return render_template('play.html', **template_context)


if __name__ == '__main__':
    app.run(port=8888)
