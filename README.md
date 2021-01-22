
run flask from Dokcer.
```bash
docker-compose up --build -d
```
if need Debug mode off.
```
# docker-compose.yml

environment:
  - FLASK_APP=server.py
 #- FLASK_ENV=development <- comment out
```

predict from base64 convert images.
```
from request_utils import predict_from_base64
from image_utils import image2base64

# endpoint for predict from base64
url = 'http://localhost:5000/predict_from_base64/'

# Image convert to base64
image_base64 = image2base64(IMAGEFILE(.jpeg or .jpg or .png))

# send predict requests
label = predict_from_base64(image_base64, url)
print(label)
```

predict from images.
```
from request_utils import predict_from_image

# endpoint for presict from image
url = 'http://localhost:5000/predict_from_image/'

# send predict requests
label = predict_from_image(IMAGEFILE(.jpeg or .jpg or .png), url)
print(label)
```

for use youe original model.
```
# server.py

# create model instance
# model = ImageModel('model folder path')
model = ImageModel('sample_model')
```
