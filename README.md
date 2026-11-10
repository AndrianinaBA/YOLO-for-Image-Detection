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
First, we need to install the library 'ultralytics' in order to run the pretrained YOLO model:
```python
pip install ultralytics
```

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

## Objective and Methods
The YOLO model is widely used in image detection, image segmentation and various computer vision tasks. For the purpose of this project, we use it for image detection on 3 classes.
To annotate the custom datasets, we used [Label Studio](https://labelstud.io/).

## Results and Analysis
The YOLO model not only predicts the classes that we assigned it to, but also create a box bound along with associated probability to tell the object that it detected inside the box.
We used the model YOLO11 but the latest version is YOLO26 that we did not use for this project.

As we see in the result folder 'runs/detect/predict-{n}', we have respectfully the boxes and the label.
A further fine-tuning or parameter-tuning could help bring more precision to the result.
However, the datasets is small and the model is already giving a good rendering.
