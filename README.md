# Agentic AI Customer Support with MLOps

## Features
- Agent-based decision making
- FAQ + AI response
- Logging with SQLite
- MLflow tracking
- Streamlit UI

## Run

### Start backend
uvicorn app.main:app --reload

### Start MLflow
mlflow ui

### Start frontend
streamlit run ui/streamlit_app.py