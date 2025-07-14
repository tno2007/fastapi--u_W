from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scraper import scrape_and_save, read_file_contents

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World!!!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# Request model for POST /scrape
class ScrapeRequest(BaseModel):
    url: str

# Response model for POST /scrape
class ScrapeResponse(BaseModel):
    url: str
    html: str

@app.post("/scrape", response_model=ScrapeResponse)
async def scrape_endpoint(request: ScrapeRequest):
    try:
        filename = scrape_and_save(request.url)
        html = read_file_contents(filename)
        return ScrapeResponse(url=request.url, html=html)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/apis/scraper")
async def scraper_hello():
    return {"message": "Hello World from /apis/scraper!!!"}