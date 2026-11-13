"""API REST com FastAPI — porta 8000 (semana 4).

Executar:  uvicorn api:app --host 0.0.0.0 --port 8000
Docs:      http://<ip-da-vm>:8000/docs
"""
from fastapi import FastAPI, HTTPException, Query

app = FastAPI(title="CTIoT — projeto-iot-lucasg")

NAO_IMPLEMENTADO = HTTPException(status_code=501, detail="TODO")


@app.get("/api/dispositivos")
def listar_dispositivos():
    """Lista de dispositivos cadastrados."""
    raise NAO_IMPLEMENTADO


@app.get("/api/dispositivos/{nome}/ultima")
def ultima(nome: str):
    """Última leitura de cada grandeza, com horário (ISO 8601 com fuso) e idade_s. 404 se não existir."""
    raise NAO_IMPLEMENTADO


@app.get("/api/dispositivos/{nome}/leituras")
def leituras(nome: str, grandeza: str, horas: int = Query(24, ge=1, le=168)):
    """Pares horário/valor de uma grandeza no período."""
    raise NAO_IMPLEMENTADO


@app.get("/api/dispositivos/{nome}/resumo")
def resumo(nome: str, horas: int = Query(24, ge=1, le=168)):
    """Mínimo, máximo, média e quantidade por grandeza."""
    raise NAO_IMPLEMENTADO
