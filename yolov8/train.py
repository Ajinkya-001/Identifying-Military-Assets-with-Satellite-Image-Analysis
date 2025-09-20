from ultralytics import YOLO

# Load your last checkpoint instead of the base yolov8s.pt
model = YOLO("yolov8s.pt")

# Resume training
model.train(
    data="/home/ajinkya/mili/yolov8/data.yaml",
    epochs=100,          
    imgsz=640,
    batch=4,
    cache=True,
    workers=4,
    device=0,
    patience=15,
    hsv_h=0.015, hsv_s=0.7, hsv_v=0.4,
    degrees=5, translate=0.1, scale=0.5, shear=2,
    mosaic=1.0, mixup=0.2,
    optimizer="AdamW",
    resume=False         
)
# Optional export
model.export(format="onnx")
