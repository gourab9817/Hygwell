from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embedding(text: str):
    return model.encode([text])

def find_most_relevant_response(content_embedding, question_embedding):
    similarity = cosine_similarity(content_embedding, question_embedding)
    # Assuming you split content into chunks; otherwise return full content.
    return "Relevant content based on cosine similarity"
