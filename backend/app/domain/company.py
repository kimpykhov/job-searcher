from pydantic import BaseModel, HttpUrl


class Company(BaseModel):
    name: str
    website: HttpUrl
    careers_url: HttpUrl
    offices: list[str]  # [vilnius, kaunas]
    ats_type: str
    ats_identifier: str
    enabled: bool
