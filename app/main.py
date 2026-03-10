from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agent import run_research_workflow

app = FastAPI(title="Multi-Agent Research Assistant")

class ResearchRequest(BaseModel):
    topic: str
    depth: str = "standard"

@app.post("/research")
async def conduct_research(request: ResearchRequest):
    try:
        result = run_research_workflow(request.topic)
        return {"topic": request.topic, "analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
