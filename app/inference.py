import os
from ultralytics import YOLO

# Load YOLOv8 model once when server starts
model = YOLO("yolov8/runs/detect/train4/weights/best.pt")

def run_inference(image_path: str, save_dir: str = "outputs") -> dict:
    """
    Run YOLOv8 inference on an image.
    Returns detections + path to annotated image.
    """
    os.makedirs(save_dir, exist_ok=True)

    results = model.predict(
        source=image_path,
        save=True,
        project=save_dir,
        name="preds",
        exist_ok=True
    )

    detections = []
    for box in results[0].boxes:
        detections.append({
            "class": int(box.cls[0]),
            "confidence": float(box.conf[0]),
            "bbox": box.xyxy[0].tolist()
        })

    annotated_path = os.path.join(results[0].save_dir, os.path.basename(image_path))

    return {
        "detections": detections,
        "annotated_path": annotated_path
    }
