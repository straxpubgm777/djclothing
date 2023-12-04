from numpy import save
from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO('yolov8n-pose.pt')

def pose_estimate(person_image):
    results = model.predict(person_image, imgsz=640, conf=0.5)

    for result in results:
        orig_img = result.orig_img
        keypoints_data = result.keypoints.data[0]

        for keypoint in keypoints_data:
            x, y, prob = keypoint.tolist()
            if prob > 0.5:
                cv2.circle(orig_img, (int(x), int(y)), 5, (0, 255, 0), -1)

        connect_lines(orig_img, keypoints_data)
        
        filtered_keypoints = [keypoint[:2] for keypoint in keypoints_data if keypoint[2] > 0.5]

        print(filtered_keypoints)
        cv2.imwrite("clients_psoe.png", cv2.cvtColor(np.array(orig_img), cv2.COLOR_BGR2RGB))

def connect_lines(image, keypoints_data):
    num_keypoints = keypoints_data.shape[0]

    # Define pairs of keypoints to connect with lines
    connections = [(5, 6), (5,11), (6,12),
                  (5, 7), (6, 8), (7, 9), (8, 10), (11, 12),
                  (11, 13), (12, 14), (13, 15), (14, 16), (0, 1), (0, 2),
                  (1, 3), (2, 4), (3, 5), (4, 6)]

    for connection in connections:
        if connection[0] < num_keypoints and connection[1] < num_keypoints:
            start_point = tuple(map(int, keypoints_data[connection[0]][:2]))
            end_point = tuple(map(int, keypoints_data[connection[1]][:2]))
            cv2.line(image, start_point, end_point, (0, 255, 0), 2)