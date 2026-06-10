def detect_intent(query):
    query = query.lower()

    if any(word in query for word in ["refund", "return", "money back"]):
        return "refund"
    
    elif any(word in query for word in ["cancel", "cancel order"]):
        return "cancel_order"
    
    elif any(word in query for word in ["order", "track", "delivery", "status"]):
        return "order_tracking"

    elif any(word in query for word in ["payment", "paid", "transaction", "failed"]):
        return "payment_issue"

    elif any(word in query for word in ["complaint", "issue", "problem", "damaged"]):
        return "complaint"

    elif any(word in query for word in ["product", "item", "details", "info"]):
        return "product_query"

    else:
        return "general"