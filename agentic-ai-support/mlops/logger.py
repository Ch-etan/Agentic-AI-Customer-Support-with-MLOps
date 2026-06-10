import mlflow

def log_to_mlflow(query, response, intent, score, source, error=False):
    mlflow.set_experiment("agentic_ai_support")

    with mlflow.start_run():
        # Params (categorical info)
        mlflow.log_param("query", query)
        mlflow.log_param("intent", intent)
        mlflow.log_param("decision", source)   # renamed for clarity (FAQ / LLM)

        # Metrics (numerical tracking)
        mlflow.log_metric("confidence_score", score)
        mlflow.log_metric("response_length", len(response))
        mlflow.log_metric("is_fallback", 1 if source == "LLM" else 0)
        mlflow.log_metric("error", 1 if error else 0)