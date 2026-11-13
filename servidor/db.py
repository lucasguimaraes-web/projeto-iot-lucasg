"""Conexão com o MySQL — usada pelo coletor e pela API (semana 3).

Regras: usuário ctiot_app (nunca root), consultas parametrizadas,
configuração lida do .env.
"""
import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def conectar():
    """Abre uma conexão com o banco ctiot."""
    # TODO: tratar reconexão quando o MySQL fechar uma conexão parada
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME", "ctiot"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
    )


def gravar_leituras(dispositivo: str, projeto: str, leituras: dict) -> None:
    """Grava uma linha por grandeza (duas por mensagem)."""
    # TODO: garantir o dispositivo em `dispositivos` e inserir em `leituras`
    raise NotImplementedError
