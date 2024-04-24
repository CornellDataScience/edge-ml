from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from deepface import DeepFace
from collections import Counter
app = FastAPI()

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

@app.post("/find/")
async def find_images(image_path: ImagePath):
    try:
        print(image_path.img_path)
        results = DeepFace.find(img_path=image_path.img_path,
                                 db_path="img_db/",
                                 model_name="GhostFaceNet")
        matches = [list(match.split("/")[1] for match in result["identity"]) if not result.empty else [] for result in results]
        
        names = [Counter(match).most_common(1)[0][0] for match in matches if match]
        
        return names
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)