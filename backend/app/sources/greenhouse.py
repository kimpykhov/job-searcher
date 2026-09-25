import json
import requests

from backend.app.domain.company import Company
from backend.app.domain.job import RawJob

company = Company(
    name="JetBrains",
    website="https://www.jetbrains.com/",
    careers_url="https://www.jetbrains.com/",
    offices=["kau", "vil"],
    ats_type="greenhouse",
    ats_identifier="jetbrains",
    enabled=True
)


# function shall receive dict for a raw jobs presented on greenhouse
def fetch_companies_data(ats_identifier):
    url = f"https://boards-api.greenhouse.io/v1/boards/{company.ats_identifier}/jobs?content=true"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Information is being written to a file for debugging purposes only; it needs to be removed for the MVP.
        with open("jetbrains_jobs.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return response.json()
    else:
        return f"error, server status-code: {response.status_code}"


company_data = fetch_companies_data(company.ats_identifier)


# function shall create some objects for a class RawJob
def normalize_jobs(data: dict):
    raw_list = []

    jobs = data["jobs"]
    # job = jobs[0]

    for job in jobs:

        new_job = RawJob(
            source=company.ats_type,
            external_id=str(job["internal_job_id"]),
            company_name=job["company_name"],
            published_at=job["first_published"],
            title=job["title"],
            location=job["location"]["name"],
            description=job["content"],
            url=job["absolute_url"]
        )

        raw_list.append(new_job)
    #print shall be removed after degug
    print(raw_list)
    return raw_list


# debug line
normalize_jobs(company_data)