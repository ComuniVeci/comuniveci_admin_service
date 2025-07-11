import requests
from fastapi import HTTPException
from src.config import AUTH_SERVICE_URL

def get_auth_metrics_summary():
    try:
        response = requests.get(f"{AUTH_SERVICE_URL}/metrics", timeout=5)
        response.raise_for_status()
        raw_metrics = response.text
        return parse_metrics(raw_metrics)
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Error al obtener métricas: {e}")

def parse_metrics(metrics_text: str):
    summary = {
    "requests_total": {},
    "request_duration_seconds": {},
    "custom_metrics": {}
    }

    for line in metrics_text.splitlines():
        line = line.strip()

        # Saltar comentarios y líneas vacías
        if not line or line.startswith("#"):
            continue

        # http_requests_total por método y handler
        if line.startswith("http_requests_total{"):
            parts = line.split()
            if len(parts) == 2:
                meta, value = parts
                try:
                    handler = meta.split('handler="')[1].split('"')[0]
                    method = meta.split('method="')[1].split('"')[0]
                    key = f"{method} {handler}"
                    summary["requests_total"][key] = float(value)
                except IndexError:
                    continue

        # http_request_duration_seconds_sum
        elif line.startswith("http_request_duration_seconds_sum{"):
            parts = line.split()
            if len(parts) == 2:
                meta, value = parts
                try:
                    handler = meta.split('handler="')[1].split('"')[0]
                    method = meta.split('method="')[1].split('"')[0]
                    key = f"{method} {handler}"
                    summary["request_duration_seconds"][key] = float(value)
                except IndexError:
                    continue

        # Extraer métricas personalizadas que empiezan por auth_ y terminan en _total
        elif line.startswith("auth_") and "_total" in line:
            parts = line.split()
            if len(parts) == 2:
                metric, value = parts
                try:
                    summary["custom_metrics"][metric] = int(float(value))
                except ValueError:
                    continue

    return summary

