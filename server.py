import base64
import json
from io import BytesIO

import cv2
import numpy as np
from flask import Flask, Response, render_template, request

from model import ImageModel

app = Flask(__name__)
model = ImageModel('sample_model')


def predict(data):
    image_dec = cv2.imdecode(data, 1).astype(np.float32) / 255.0
    x = np.expand_dims(image_dec, axis=0)
    label = model.predict(x)
    return label


@ app.route('/predict_from_base64/', methods=['POST'])
def predict_from_base64():
    data_json = json.loads(request.data)
    image_bytes = base64.b64decode(data_json['image'])
    image_np = np.frombuffer(image_bytes, dtype='uint8')
    label = predict(image_np)
    return Response(json.dumps({'label': label}))


@ app.route('/predict_from_image/', methods=['POST'])
def predict_from_image():
    file = request.files['file']
    if not file.filename:
        return Response(json.dumps({'message': 'image not found'}))
    buff = BytesIO()
    file.save(buff)
    image_np = np.frombuffer(buff.getvalue(), dtype='uint8')
    label = predict(image_np)
    return Response(json.dumps({'label': label}))


@ app.route('/upload_image/', methods=['GET'])
def upload_file():
    return render_template('upload_image.html')
