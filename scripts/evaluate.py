from ultralytics import YOLO

def evaluate():
    model = YOLO("yolov8/runs/detect/train4/weights/best.pt")
    metrics = model.val(data="yolov8/data.yaml")
    print(metrics)

if __name__ == "__main__":
    evaluate()
