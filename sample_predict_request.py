from request_utils import predict_from_base64, predict_from_image
from image_utils import image2base64

url = 'http://localhost:5000/predict_from_base64/'
image_base64 = image2base64('sample_image/cat/cat.104.jpg')
label = predict_from_base64(image_base64, url)
print(f'predict_from_base64: {label}')

url = 'http://localhost:5000/predict_from_image/'
label = predict_from_image('sample_image/dog/dog.103.jpg', url)
print(f'predict_from_image: {label}')
