# scripts/visualize.py
import cv2
import numpy as np
from ultralytics import YOLO

MODEL_PATH = "yolov8/runs/detect/train4/weights/best.pt"
model = YOLO(MODEL_PATH)

def visualize_inference(image_bytes: bytes):
    """Run YOLO inference and return image with drawn boxes (bytes)."""
    # Convert bytes → NumPy image
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Run YOLO
    results = model.predict(img)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = model.names[int(box.cls)]
            conf = float(box.conf)

            # Draw bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, f"{cls} {conf:.2f}",
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 255, 0), 2)

    # Encode back to bytes (JPEG)
    _, buffer = cv2.imencode(".jpg", img)
    return buffer.tobytes()
