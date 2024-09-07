from uuid import uuid4

# In-memory storage for demo purposes (replace with DB for production)
storage = {}

def store_content(content: str) -> str:
    chat_id = str(uuid4())
    storage[chat_id] = content
    return chat_id

def retrieve_content(chat_id: str) -> str:
    return storage.get(chat_id)
