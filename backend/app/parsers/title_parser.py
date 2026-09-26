# function shall return only seniority of user
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
        if role in title_mapping:
            title_value = title_mapping[role]
    return title_value


# debug to be removed
print((seniority_parser("SR QA Engineer")))


# ToDo if order in phrase will be different, function might be broken. Rework is must.
# function shall return only role of user
def role_parser(data):
    # dict for allowed role values
    role_mapping = {
        "qa": "qa", "quality": "qa", "test": "qa", "tester": "qa",
        "developer": "developer", "dev": "developer", "programmer": "developer",
        "ml": "ml", "ai": "ml", "ds": "ml", "data scientist": "ml",
        "pm": "pm", "manager": "pm", "ba": "ba", "analyst": "ba",
        "designer": "designer", "ux": "designer", "ui": "designer"
    }

    roles = data.lower().split()

    role_value = None

    for role in roles:
        if role in role_mapping:
            role_value = role_mapping[role]
            break
    return role_value


# debug to be removed
print((role_parser("SR QA Engineer")))


# ToDo Senior Data Scientist wouldn't work because of lost value on the dict.
# function shall return only specialization of user
def specialization_parser(data):
    # dict for allowed specialization values
    specialization_mapping = {
        "automation": "automation", "autotest": "automation", "автомейшен": "automation", "автоматизатор": "automation",
        "manual": "manual", "мануал": "manual", "ручной": "manual",
        "performance": "performance", "load": "performance", "перформанс": "performance", "нагрузочное": "performance",
        "frontend": "frontend", "front-end": "frontend", "фронтэнд": "frontend", "фронтенд": "frontend",
        "backend": "backend", "back-end": "backend", "бэкэнд": "backend", "бэкенд": "backend",
        "fullstack": "fullstack", "full-stack": "fullstack", "фуллстек": "fullstack",
        "ios": "ios", "android": "android", "andriod": "android", "mobile": "mobile", "мобильный": "mobile",
        "nlp": "nlp", "cv": "cv", "vision": "cv",
        "none": "none", "nan": "none", "нан": "none"
    }

    specializations = data.lower().split()

    specialization_value = None

    for spec in specializations:
        if spec in specialization_mapping:
            specialization_value = specialization_mapping[spec]
            break
    return specialization_value


# debug to be removed
print((specialization_parser("Senior Data Scientist")))


# goal of the function to connect all the previous functions and return whole parsed_title/result
def title_parser(data):
    title = {
        "role": role_parser(data),
        "seniority": seniority_parser(data),
        "specialization": specialization_parser(data)
    }
    return title


# debug to be removed
print((title_parser("SR QA Engineer")))

