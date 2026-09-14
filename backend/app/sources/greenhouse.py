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


COMPANY_TOKEN = "jetbrains"

# todo token for jetbrains - temporary solution, later to be adjusted for a list
url = f"https://boards-api.greenhouse.io/v1/boards/{COMPANY_TOKEN}/jobs"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # todo to remove store on disk. shall return the value
    with open("jetbrains_jobs.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

else:
    print(f"error, server status-code: {response.status_code}")
