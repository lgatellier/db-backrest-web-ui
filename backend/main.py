from fastapi import FastAPI

app = FastAPI()

@app.get("/applications")
async def applications():
    return [{
        "id": "app1",
        "fullName": "Application 1"
    }]

@app.get("/applications/{app_id}")
async def application(app_id: str):
    return {
        "id": app_id,
        "fullName": app_id[0:1].upper() + app_id[1:]
    }

@app.get("/applications/{app_id}/environments")
async def environments(app_id: str):
    app = await application(app_id)

    return [{
        "id": "prod",
        "fullName": f"{app['fullName']} Production",
        "production": True
    }, {
        "id": "staging",
        "fullName": f"{app['fullName']} Staging",
        "production": False
    }]
