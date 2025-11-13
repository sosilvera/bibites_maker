from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from models.models import ProcessRequest
import commons.utils as utils
import os
import tempfile

router = APIRouter(prefix="/bibites")

RESOURCE_DIR = os.path.join("static", "resources")

@router.get("/list")
def list_bibites():
    try:
        files = [f for f in os.listdir(RESOURCE_DIR) if f.endswith(".bb8template")]
        return {"files": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/process")
def process_bibite(req: ProcessRequest):
    file_path = os.path.join(RESOURCE_DIR, req.file)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")

    with open(file_path, "r", encoding="utf-8") as f:
        bibite_data = f.read()

    new_text = utils.process_info(bibite_data, req.instructions)

    # Validar contenido
    if "{" in new_text and "}" in new_text:
        json_only = new_text[new_text.index("{"):new_text.rindex("}") + 1]
    else:
        raise HTTPException(status_code=400, detail="No se encontró un JSON válido en la respuesta del modelo.")

    # Guardar en archivo temporal
    new_filename = req.file.replace(".bb8template", "_nuevo.bb8template")
    save_path = os.path.join(tempfile.gettempdir(), new_filename)

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(json_only)

    # Enviar como descarga
    return FileResponse(
        path=save_path,
        filename=new_filename,
        media_type="application/octet-stream"
    )
