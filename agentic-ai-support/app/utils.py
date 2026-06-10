import json

def load_faq():
    with open("data/faq.json") as f:
        return json.load(f)