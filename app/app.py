from fastapi import FastAPI, Security,Depends, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKey
from pydantic import BaseModel
from typing import List
from app.db.mongo import *
from dotenv import load_dotenv
import json

from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import JSONResponse

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')
DATABASE = os.getenv('DATABASE')
COLLECTION = os.getenv('COLLECTION')
API_KEY = os.getenv('API_KEY')
API_KEY_NAME = "apiKey"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key_query: str = Security(api_key_query)):
    if api_key_query == API_KEY:
        return api_key_query
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


class Jobs(BaseModel):
    job_id: str
    job_title: str
    company: str
    job_post_date: str
    job_requirement_career_level: str
    company_size: str
    company_industry: str
    job_description: str
    job_employment_type: str
    job_function: str

app = FastAPI(redoc_url=None)
db = Mongo(MONGO_URL, DATABASE, COLLECTION)


@app.get("/jobs/")
async def index_job(api_key: APIKey = Depends(get_api_key)):
    return db.index()

@app.get("/jobs/{job_id}")
async def show_job(job_id, api_key: APIKey = Depends(get_api_key)):
    return db.show(job_id)

@app.post("/jobs/")
async def upsert_job(jobs: List[Jobs], api_key: APIKey = Depends(get_api_key)):
    return db.upsert([job.__dict__ for job in jobs])

