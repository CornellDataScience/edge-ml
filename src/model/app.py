from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from deepface import DeepFace
from collections import Counter
from PIL import Image
from io import StringIO
import tensorflow as tf

app = FastAPI()

print(tf.test.is_gpu_available())

class ImagePaths(BaseModel):
    img1_path: str
    img2_path: str

class ImagePath(BaseModel):
    img_path: str

@app.post("/verify/")
async def verify_images(image_paths: ImagePaths):
    try:
        result = DeepFace.verify(img1_path=image_paths.img1_path, 
                                 img2_path=image_paths.img2_path, 
                                 model_name="GhostFaceNet")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/save/")
async def save_images(image):
    try:
        print(image[:100])
        # im = Image.open(StringIO(bytes))
        # im.save("face.jpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/save2/")
async def find_images(image_file: UploadFile = File(...)):
    try:
        # Save the uploaded image to a specified location
        with open("image.jpg", "wb") as f:
            f.write(await image_file.read())

        # Process the saved image as needed (e.g., perform face recognition)
        # Here, we simply return a success message
        return JSONResponse(content={"message": "Image received and saved successfully"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/find/")
async def find_images():
    try:
        results = DeepFace.find(img_path="face.jpeg",
                                 db_path="img_db/",
                                 detector_backend="ssd",
                                 model_name="GhostFaceNet")
        matches = [list(match.split("/")[1] for match in result["identity"]) if not result.empty else [] for result in results]
        
        names = [Counter(match).most_common(1)[0][0] for match in matches if match]
        
        return names
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="10.49.25.69", port=8001)
