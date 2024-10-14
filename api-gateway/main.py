# api-gateway/main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()


@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def api_gateway(request: Request, path: str):
    # Route to appropriate microservice based on path
    if path.startswith("user"):
        service_url = "http://user-service:8000"
    elif path.startswith("post"):
        service_url = "http://post-service:8000"
    elif path.startswith("community"):
        service_url = "http://community-service:8000"
    else:
        return JSONResponse({"error": "Service not found"}, status_code=404)

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=f"{service_url}/{path}",
            headers=request.headers,
            params=request.query_params,
            content=await request.body()
        )

    return JSONResponse(
        content=response.json(),
        status_code=response.status_code,
        headers=dict(response.headers)
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
