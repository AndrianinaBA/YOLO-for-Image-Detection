This repository serves as the Final Project for Computer Vision in Computer, for the class M2 in MAFI and Maths Struct at the University of Antananarivo.
Also, it contributes as an initiation into the rich field of Computer Vision by using Image Detection.

## Base Model
This project uses [YOLO11](https://docs.ultralytics.com/models/yolo11/) for object detection.

## Datasets
The model was trained using a custom dataset derived from the [COCO (Common Objects in Context) dataset](https://cocodataset.org/).
We selected images from the datasets containing the following classes:
 - car
 - person
 - train

## How to run?
To re-run the model, use:
```python
python train.py

```

To run inference on the new images, go to the 'val' folder, select the name of the image, and paste it into the file named 'predict_yolo.py':

```python
IMAGE_PATH = (
    PROJECT_DIR
    / "val"
    / "images"
    / "9827778906_f6e78c7551_z.jpg" # Line to replace
)
```
And run:
```python
python predict_yolo.py
```

The result will be under the folder 'runs/detect/' and 'predict-{n}'.
