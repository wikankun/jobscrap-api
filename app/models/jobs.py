from pydantic import BaseModel

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
