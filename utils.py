import requests
from bs4 import BeautifulSoup

def scrape_url_content(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text(separator=' ').strip()
    return ' '.join(content.split())

import PyPDF2

def extract_pdf_text(file) -> str:
    reader = PyPDF2.PdfReader(file.file)
    content = ""
    for page in reader.pages:
        content += page.extract_text()
    return ' '.join(content.split())

