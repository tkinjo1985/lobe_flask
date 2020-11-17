from request_utils import predict_from_base64, predict_from_image
from image_utils import preprocess_image

url = 'http://localhost:5000/predict_from_base64/'

image_base64 = preprocess_image('sample_image/cat/cat.102.jpg', 224, 224)
label = predict_from_base64(image_base64, url)
print(label)

# url = 'http://localhost:5000/predict_from_image/'
# label = predict_from_image('sample_image/cat/cat.103.jpg', url)
# print(label)
