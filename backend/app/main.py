from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timezone

app=FastAPI(title="Legal Platform Cloud Demo API", version="108.0-demo")

class Login(BaseModel):
    username:str
    password:str

@app.get("/api/health")
def health():
    return {"status":"ok","environment":"demo","timestamp":datetime.now(timezone.utc).isoformat()}

@app.get("/api/dashboard")
def dashboard():
    return {"active_matters":27,"decisions_pending":6,"high_risks":3,"audit_events":2941}

@app.post("/api/demo/login")
def login(payload:Login):
    if payload.password!="demo123":
        return {"authenticated":False}
    return {"authenticated":True,"username":payload.username,"role":payload.username,"demo":True}
