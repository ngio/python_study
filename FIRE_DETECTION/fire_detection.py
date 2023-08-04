"""_summary_
    python fire detection
    
    pip install tensorflow opencv-python
"""
import cv2
import numpy as np

import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
real_path = Path(__file__).parent.parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 


# Load YOLO model
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
with open("yolov3.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Load image and prepare for detection
def detect_fire(image_path):
    img = cv2.imread(image_path)
    height, width = img.shape[:2]

    # YOLO expects the image in blob format
    blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)

    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layer_outputs = net.forward(output_layers_names)

    conf_threshold = 0.5
    nms_threshold = 0.4

    # Loop over each output layer and detect objects
    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > conf_threshold and classes[class_id] == "fire":
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Calculate bounding box coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                # Draw bounding box and label on the image
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, "Fire", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Fire Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = real_path &"/img/img_01.jpg"
    detect_fire(image_path)
