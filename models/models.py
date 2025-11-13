from pydantic import BaseModel

# Modelos Pydantic para las solicitudes y respuestas

class ProcessRequest(BaseModel):
    file: str
    instructions: str
