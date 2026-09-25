def title_parser(data):
    # dict for allowed title values
    title_dict = ["senior", "sen.", "sr", "sr.", "middle", "mid.", "junior", "jun."]

    # creation of list to split the values
    titles = data.lower().split()

    title_value = None

    for role in title_dict:
        if role in titles:
            title_value = role
    return title_value


print((title_parser("SR QA Engineer")))