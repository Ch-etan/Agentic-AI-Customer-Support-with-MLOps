from app.semantic import semantic_search
from app.utils import load_faq
from app.memory import add_to_memory
from app.intent import detect_intent
from app.model import generate_response

faq = load_faq()

def agent_response(query):
    intent = detect_intent(query)

    best_match, score = semantic_search(query)

    # Decision logic
    if score > 0.73:
        response = faq[best_match]
        decision = "FAQ"
        error = False
    else:
        try:
            response = generate_response(query)
            decision = "LLM"
            error = False
        except:
            response = "Sorry, something went wrong."
            decision = "ERROR"
            error = True

    add_to_memory(query, response)

    return response, intent, score, decision, error