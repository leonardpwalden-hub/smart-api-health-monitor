from fastapi import FastAPI
import requests
import time

app = FastAPI(
    title="Smart API Health Monitor",
    description="Monitor API health, response times and endpoint availability.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "Smart API Health Monitor",
        "status": "running"
    }


@app.get("/health-check")
def health_check(url: str):

    start_time = time.time()

    try:
        response = requests.get(url, timeout=10)

        response_time = round(
            (time.time() - start_time) * 1000,
            2
        )

        return {
            "url": url,
            "status": "UP",
            "status_code": response.status_code,
            "response_time_ms": response_time
        }

    except Exception as e:

        return {
            "url": url,
            "status": "DOWN",
            "error": str(e)
        }