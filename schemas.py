from pydantic import BaseModel, Field

class CafeSchema(BaseModel):
    nome: str = Field(..., description="Nome do café")
    produtor: str = Field(..., description="Produtor do café")
    variedade: str = Field(..., description="Variedade do café")
    processo: str = Field(..., description="Processo do café")
    sensorial_docura: int = Field(..., description="Docura")
    sensorial_acidez: int = Field(..., description="Acidez")
    sensorial_corpo: int = Field(..., description="Corpo")
    sensorial_amargor: int = Field(..., description="Amargor")
