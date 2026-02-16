from fastapi import FastAPI

app = FastAPI(title="Generative AI Learning Lab API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
