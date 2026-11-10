from ultralytics import YOLO

model = YOLO("yolo11m.pt")

model.train(
        data="dataset.yaml",
        imgsz=640,
        batch=4,
        epochs=100,
        workers=0,
        device=0
        )
