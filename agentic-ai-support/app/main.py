from fastapi import FastAPI
from app.agent import agent_response
from app.database import init_db, log_data
from mlops.logger import log_to_mlflow

app = FastAPI()
init_db()

@app.get("/chat")
def chat(query: str):
    response, intent, score, decision, error = agent_response(query)

    log_data(query, response)

    log_to_mlflow(
        query=query,
        response=response,
        intent=intent,
        score=score,
        source=decision,
        error=error
    )

    return {
        "response": response,
        "intent": intent,
        "confidence": float(score),
        "decision": decision
    }