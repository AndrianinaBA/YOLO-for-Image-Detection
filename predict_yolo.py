# from ultralytics import YOLO

# folder_name = "/home/supercell/Desktop/YOLO_project/runs/detect/train-3/weights/"
# image_val_folder = "/home/supercell/Desktop/YOLO_project/val/images/"

# image_file_name = image_val_folder + "9646832678_3027b999de_z.jpg"

# model_predict = YOLO(folder_name + "best.pt")

# model_predict.predict(
#         source=image_file_name,
#         show=True,
#         save=True,
#         )
        

from pathlib import Path
from ultralytics import YOLO

# Get the directory containing this script
PROJECT_DIR = Path(__file__).resolve().parent

# Define paths relative to the project directory
MODEL_PATH = PROJECT_DIR / "runs" / "detect" / "train-3" / "weights" / "best.pt"

IMAGE_PATH = (
    PROJECT_DIR
    / "val"
    / "images"
    / "9827778906_f6e78c7551_z.jpg"
)

# Load model
model = YOLO(str(MODEL_PATH))

# Perform prediction
results = model.predict(
    source=str(IMAGE_PATH),
    show=True,
    save=True,
)


