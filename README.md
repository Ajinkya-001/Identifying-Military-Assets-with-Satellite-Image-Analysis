![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.1-red?logo=pytorch&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.101-green?logo=fastapi&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-2.9-blue)
![Docker](https://img.shields.io/badge/Docker-24.0-blue?logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

# Identifying Military Assets with Satellite Image Analysis

## Project Overview

This project leverages YOLOv8 object detection and satellite imagery to automatically identify and 
map military infrastructure. Designed for real-time analysis, it integrates FastAPI for API 
serving and provides clear geospatial visualizations of detected assets.

## Key Highlights:

Detection of military facilities from high-resolution satellite imagery

Fast and scalable inference using YOLOv8

Integrated with FastAPI for API deployment

Designed for potential deployment in defense-tech R&D and advanced geospatial intelligence systems

## Dataset Preparation

The model was trained on a custom dataset of satellite imagery. The raw dataset is available here - https://drive.google.com/drive/folders/1JhbzmCQK6aqwd33azx9k4zvuqr7FXZ_A?usp=sharing

### Important Note: 
The provided dataset contains raw images and their corresponding label files. To use it for training this YOLOv8 model, you must perform the following preparation steps:

Dataset Splitting: You need to split the data into training, validation, and test sets (e.g., 70%/20%/10%). This can be done using scripts from the scripts/ directory.

Label Format Conversion: Ensure the label files are converted to the correct format expected by YOLOv8 (typically .txt files with one file per image, containing class_id center_x center_y width height normalized to 0-1).

The repository includes utility scripts (scripts/split_dataset.py, scripts/convert_labels.py) to help automate this process. Please refer to the comments within those scripts for usage instructions.

###After preparation, your dataset directory should be structured as follows:

<img width="441" height="284" alt="image" src="https://github.com/user-attachments/assets/59201f2e-25c3-40ae-a1f4-b556d4414100" />


## Directory Structure

<img width="724" height="259" alt="image" src="https://github.com/user-attachments/assets/fb8504aa-b404-49c4-8582-34d4674ded52" />

## Setup & Installation

1. Clone the repo:
   ```
   git clone git@github.com:Ajinkya-001/Identifying-Military-Assets-with-Satellite-Image-Analysis.git
   cd Identifying-Military-Assets-with-Satellite-Image-Analysis
   ```
2. Create a virtual environment & install dependencies:
   ```
   python -m venv yolo_env
   source yolo_env/bin/activate
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```
   uvicorn app.main:app --reload
   ```
   
## Usage

Access the API at http://localhost:8000/

Send satellite images for military asset detection

Receive detection results with bounding boxes and confidence scores

### Visualization

Detected bounding boxes can be overlaid on images for quick analysis.

<img width="959" height="898" alt="image" src="https://github.com/user-attachments/assets/2b946939-b53f-4e30-99b5-3fbe7b9d288d" />


## Training Results

<img width="2400" height="1200" alt="image" src="https://github.com/user-attachments/assets/7006120d-15e8-4c1d-955e-8df8a26c0ab5" />


## Results (Final Epoch)

### Training Losses

Box loss: 1.434

Cls loss: 0.842

DFL loss: 0.916

### Validation Losses

Box loss: 1.466

Cls loss: 0.867

DFL loss: 0.920

### Metrics 

Precision (B): 85.8%

Recall (B): 44.9%

mAP@50 (B): 50.9%

mAP@50-95 (B): 28.6%

### Confusion Matrix

The normalized confusion matrix below shows class-wise prediction accuracy and misclassifications:


<img width="3000" height="2250" alt="image" src="https://github.com/user-attachments/assets/f2445925-c748-4438-aa70-5b8b4211470b" />

### interpretation of your matrix

Fighter jet: 64% correctly classified, but often confused with background.

Radar: strongest detection (74% correct).

Tank: seems underrepresented (little data or poor detection).

Military truck: confused with background often.

Background: relatively well recognized (71%), but sometimes objects are misclassified as background.



## Future Enhancements

Real-time streaming satellite data processing

Integration with geospatial visualization dashboards

Multi-class military asset classification

## Acknowledgements

YOLOv8-Object detection framework

Open satellite datasets – Training and validation

FastAPI – API framework

## Author

Ajinkya Patil

LinkedIn : https://www.linkedin.com/in/ajinkya-patil-728a19313/











