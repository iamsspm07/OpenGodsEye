from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import fuzz

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_identity(name, profiles):
    if not profiles:
        return []

    texts = [name] + [p.get("title","") for p in profiles]
    emb = model.encode(texts)
    scores = cosine_similarity([emb[0]], emb[1:])[0]

    for i,p in enumerate(profiles):
        fuzzy = fuzz.token_sort_ratio(name, p.get("title","")) / 100
        p["confidence"] = round(float(scores[i]*0.7 + fuzzy*0.3), 2)

    return profiles