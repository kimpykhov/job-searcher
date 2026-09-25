def seniority_parser(data):
    # dict for allowed title values
    title_mapping = {
        "senior": "senior", "sen.": "senior", "sr": "senior", "sr.": "senior",
        "middle": "middle", "mid.": "middle", "mid": "middle",
        "junior": "junior", "jun.": "junior", "jun": "junior"
    }

    # creation of list to split the values
    titles = data.lower().split()

    title_value = None

    for role in titles:
        # ToDo need to add else block, for cases that's weren't predicted as type None
        if role in title_mapping:
            title_value = title_mapping[role]
    return title_value


print((seniority_parser("SR QA Engineer")))


def role_parser(data):
    pass


def specialization_parser(data):
    pass

