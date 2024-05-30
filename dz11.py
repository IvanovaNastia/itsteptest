import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def load_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

input_image_path = 'koti.jpg'
img = load_image(input_image_path)

results = model(img)

detections = results.xyxy[0].numpy()
confidence_threshold = 0.3
filtered_detections = [detection for detection in detections if detection[4] > confidence_threshold]
coordinates = [(int(x1), int(y1), int(x2), int(y2)) for x1, y1, x2, y2, conf, cls in filtered_detections]

overlay_image_path = 'cobaka.jpg'
overlay_img = cv2.imread(overlay_image_path, cv2.IMREAD_UNCHANGED)

def overlay_image(background, overlay, coordinates):
    for (x1, y1, x2, y2) in coordinates:
        overlay_resized = cv2.resize(overlay, (x2 - x1, y2 - y1))
        alpha_s = overlay_resized[:, :, 3] / 255.0 if overlay_resized.shape[2] == 4 else 1
        alpha_l = 1.0 - alpha_s

        for c in range(0, 3):
            background[y1:y2, x1:x2, c] = (alpha_s * overlay_resized[:, :, c] + alpha_l * background[y1:y2, x1:x2, c])

overlay_image(img, overlay_img, coordinates)

cv2.imshow("Result", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
cv2.waitKey()
cv2.destroyAllWindows()
