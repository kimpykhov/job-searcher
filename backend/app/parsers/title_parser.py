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


# debug to be removed
print((seniority_parser("SR QA Engineer")))


def role_parser(data):
    # dict for allowed role values
    role_mapping = {
        "qa": "qa", "quality": "qa", "test": "qa", "tester": "qa", "тестировщик": "qa", "куа": "qa",
        "developer": "developer", "dev": "developer", "engineer": "developer", "programmer": "developer",
        "разработчик": "developer", "дев": "developer", "программист": "developer", "инженер": "developer",
        "ml": "ml", "ai": "ml", "ds": "ml", "data scientist": "ml", "мль": "ml", "ии": "ml",
        "pm": "pm", "manager": "pm", "менеджер": "pm", "ba": "ba", "analyst": "ba", "аналитик": "ba",
        "designer": "designer", "ux": "designer", "ui": "designer", "дизайнер": "designer"
    }

    roles = data.lower().split()

    role_value = None

    for role in roles:
        # ToDo need to add else block, for cases that's weren't predicted as type None
        if role in role_mapping:
            role_value = role_mapping[role]
            break
    return role_value


def specialization_parser(data):
    pass


# debug to be removed
print((role_parser("SR QA Engineer")))

