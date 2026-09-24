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
    url = f"https://boards-api.greenhouse.io/v1/boards/{company.ats_identifier}/jobs"

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
def normalize_jobs(company_data):
    raw_list = []
    new_job = []

    job = company_data["jobs"][0]
    external_id = job["internal_job_id"]
    company_name = job["company_name"]
    published_at = job["first_published"]
    title = job["title"]
    location = job["location"]["name"]
    url = job["absolute_url"]

    new_job.extend([external_id, company_name, published_at, title, location, url])

    #debug line
    print(url)

    return raw_list.append(new_job)

#debug line
normalize_jobs(company_data)