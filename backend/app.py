from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
from mangum import Mangum
import shutil

app = FastAPI(root_path="/")

model = YOLO("yolov8n.pt")

@app.get("/")
async def root():
    return {
        "message": "Bottle Detection API",
        "endpoints": {
            "POST /detect": "Upload image to detect bottles"
        },
        "usage": "POST to /detect with form-data file=<image>"
    }

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    
    image_path = file.filename
    
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    results = model(image_path)
    
    bottle_detected = False
    detected_objects = []
    
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = model.names[cls_id]
        
        detected_objects.append({
            "object": class_name,
            "confidence": round(confidence, 2)
        })
        
        if class_name in ["bottle", "vase"]:
            bottle_detected = True
    
    return {
        "bottle_detected": bottle_detected,
        "detected_objects": detected_objects
    }

handler = Mangum(app)