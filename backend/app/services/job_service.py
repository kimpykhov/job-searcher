from backend.app.parsers.title_parser import title_parser
from backend.app.domain.job import RawJob


# function shall receive and return all normalized jobs
def parse_all_jobs(raw_jobs: list[RawJob]):
    parsed_jobs = []

    for raw_job in raw_jobs:
        parsed_jobs.append(title_parser(raw_job.title))
    return parsed_jobs


print(parse_all_jobs())


