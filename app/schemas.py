from pydantic import BaseModel
from typing import List, Dict, Any

class DetectionResponse(BaseModel):
    filename: str
    detections: List[Dict[str, Any]]
