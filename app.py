import csv
import codecs
import os
import time

from flask import (Flask, flash, jsonify, request,
                   redirect, send_from_directory, url_for)
from tqdm import tqdm
from werkzeug.utils import secure_filename

from .db import dbs as db

UPLOAD_FOLDER = './uploads'
SECRET_KEY = '\xbc\xe1,\xf08\xef\x7f\x05\xf7\x8dEs>\x87v\xde+&\xa7\xfe\xd4[B.\xb0'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return 'Hello world!'


index = 0
flag = False
paused = False
data = []
row_count = 0
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    try:
        if request.method == 'POST':
            db.uploadtest.remove({})

            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                global data
                global flag
                global paused
                global index
                global row_count
                with open(filename, 'r') as fl:
                    spamreader = csv.reader(codecs.iterdecode(file, 'utf-8'))
                    row_count = sum(1 for row in fl)
                count = 0
                data = []
                head_list = []
                flag = False
                paused = False
                print('Processing the Upload')
                iterator = tqdm(spamreader, total=row_count)
                for row in iterator:
                    time.sleep(0.1)
                    index = count
                    if flag == True:
                        break
                    if paused == True:
                        index = count
                        while paused:
                            time.sleep(0.1)
                    if count == 0:
                        head_list = row
                        count += 1
                    else:
                        data.append(dict(zip(head_list, row)))
                        count += 1

                print('Complete/Finish')

                if flag == False:
                    db.uploadtest.insert(data)

                file.save(os.path.join(app.root_path,
                                       app.config['UPLOAD_FOLDER'], filename))

                return jsonify({'code': '1',
                                'Message': 'Succesfully added file to database',
                                'status': 'success'})
        else:
            return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>Upload new File</h1>
            <form method=post enctype=multipart/form-data>
              <input type=file name=file>
              <input type=submit value=Upload>
            </form>
            '''
    except Exception as e:
        print('ERROR:', e)
        return f'ERROR: {e}'


@app.route('/pause', methods=['GET', 'POST'])
def pause():
    global paused, index, row_count
    paused = True
    return f'paused at row {index+1}/{row_count}\n'


@app.route('/resume', methods=['GET', 'POST'])
def resume():
    global paused, index, row_count
    paused = False
    return f'resumed from row {index}/{row_count}\n'


@app.route('/terminate', methods=['GET', 'POST'])
def terminate():
    global flag
    flag = True
    return jsonify({'code': '0',
                    'Message': 'Fail to process/Force stopped',
                    'status': 'fail'})


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
