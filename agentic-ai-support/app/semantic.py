from sentence_transformers import SentenceTransformer, util
from app.utils import load_faq

faq = load_faq()
questions = list(faq.keys())

model = SentenceTransformer('all-MiniLM-L6-v2')

faq_embeddings = model.encode(questions, convert_to_tensor=True)

def semantic_search(query):
    query_embedding = model.encode(query, convert_to_tensor=True)
    
    scores = util.cos_sim(query_embedding, faq_embeddings)
    
    best_score = scores.max().item()
    best_index = scores.argmax().item()

    return questions[best_index], best_score