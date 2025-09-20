from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
import shutil, os
from app.inference import run_inference

app = FastAPI(
    title="Military Infra Detection API 🚀",
    description="Upload satellite images to detect **fighter jets, tanks, radars, ships, trucks** using YOLOv8.",
    version="1.0.0",
)

@app.get("/", tags=["Health Check"])
def root():
    """
    Check API health.
    """
    return {"status": "ok", "message": "YOLOv8 Military Infra Detection API running"}

@app.post("/predict", tags=["Inference"])
async def predict(file: UploadFile = File(...)):
    """
    Upload an image for detection.  
    Returns JSON with detections and a link to the annotated image.
    """
    try:
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = run_inference(temp_path)

        response = {
            "detections": result["detections"],
            "annotated_image_url": f"/annotated/{os.path.basename(result['annotated_path'])}"
        }

        return JSONResponse(content=response)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/annotated/{filename}", tags=["Results"])
async def get_annotated(filename: str):
    """
    Fetch the annotated image by filename.
    """
    file_path = os.path.join("outputs", "preds", filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="image/jpeg")
    return JSONResponse(content={"error": "File not found"}, status_code=404)
