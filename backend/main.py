import os
import shutil

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.pipeline_schemas import PipelineSchema
from app.builder import build_pipeline_from_json
from app.core.exceptions import InfoflowError

app = FastAPI(title="Infoflow Studio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):

    # Crear carpeta si no existe
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Guardar archivo en disco
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "status": "success",
        "filename": file.filename,
        "path": file_path
    }

@app.post("/execute")
def execute_pipeline(pipeline_data: PipelineSchema):
    """
    Recibe un pipeline en formato JSON,
    lo construye y lo ejecuta.
    """

    try:
        pipeline = build_pipeline_from_json(pipeline_data)

        result_df = pipeline.execute(pipeline_data.target)

        # Convertimos DataFrame a JSON serializable
        result_json = result_df.to_dict(orient="records")

        return {
            "status": "success",
            "rows": len(result_json),
            "data": result_json
        }

    except InfoflowError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))