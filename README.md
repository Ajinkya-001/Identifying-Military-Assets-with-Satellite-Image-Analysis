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









