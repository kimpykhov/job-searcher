import json
import requests

from backend.app.domain.company import Company

company = Company(
    name="JetBrains",
    website="https://www.jetbrains.com/",
    careers_url="https://www.jetbrains.com/",
    offices=["kau", "vil"],
    ats_type="greenhouse",
    ats_identifier="jetbrains",
    enabled=True
)


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

