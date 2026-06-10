import requests

def generate_response(query):
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3.5",
                "prompt": f"""
You are a customer support AI for an e-commerce platform named H-Mart. Answer in 20 to 40 words maximum. Your name is Evo.
User: {query}
""",
                "stream": False
            },
        )

        data = res.json()
        return data.get("response", "No response from model.")

    except Exception as e:
        return f"Error: {str(e)}"