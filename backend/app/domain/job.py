from pydantic import BaseModel, HttpUrl
from typing import Literal
from datetime import datetime


class RawJob(BaseModel):
    source: str
    external_id: int
    company_name: str
    published_at: datetime
    title: str  # "Sr. QA Automation Engineer (m/f/d)"
    location: str  # "Vilnius, LT / Hybrid"
    description: str
    url: HttpUrl


class Job(BaseModel):
    external_id: str
    published_at: datetime
    company_name: str
    description: str
    url: HttpUrl
    country: str | None
    city: str | None
    workplace: Literal["hybrid", "on-site", "remote"] | None  # hybrid/on-site/remote
    title: str  # sr qa automation etc
    role: str  # qa
    seniority: str
    specialization: str | None
