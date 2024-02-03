import cv2
import torch
from PIL import Image
import pprint

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model.to("cuda")
print(model.stride)
# # Images
# for f in 'zidane.jpg', 'bus.jpg':
#     torch.hub.download_url_to_file('https://ultralytics.com/images/' + f, f)  # download 2 images
# im1 = Image.open('zidane.jpg')  # PIL image
# im2 = cv2.imread('bus.jpg')[..., ::-1]  # OpenCV image (BGR to RGB)

# # Inference
# results1 = model([im1, im2], size=640)  # batch of images
# model.to("cpu")
# results2 = model([im1, im2], size=640)  # batch of images
# # Results
# print(results1)
# print(results2)
