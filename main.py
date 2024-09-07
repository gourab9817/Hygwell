from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.utils import scrape_url_content
from app.storage import store_content

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/process_url")
async def process_url(request: URLRequest):
    try:
        content = scrape_url_content(request.url)
        chat_id = store_content(content)
        return {"chat_id": chat_id, "message": "URL content processed and stored successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI, UploadFile, File, HTTPException
from app.utils import extract_pdf_text
from app.storage import store_content

@app.post("/process_pdf")
async def process_pdf(file: UploadFile = File(...)):
    try:
        content = extract_pdf_text(file)
        chat_id = store_content(content)
        return {"chat_id": chat_id, "message": "PDF content processed and stored successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.embeddings import generate_embedding, find_most_relevant_response
from app.storage import retrieve_content

class ChatRequest(BaseModel):
    chat_id: str
    question: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        content = retrieve_content(request.chat_id)
        if not content:
            raise HTTPException(status_code=404, detail="Content not found")
        
        content_embedding = generate_embedding(content)
        question_embedding = generate_embedding(request.question)
        
        response = find_most_relevant_response(content_embedding, question_embedding)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
