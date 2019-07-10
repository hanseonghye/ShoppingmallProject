def hello_ko():
    return "안녕"


def hello_en():
    return "Hello"


def hello_repeat(lang, rep):
    if lang == 'ko':
        hello_str = hello_ko()
    elif lang == 'en':
        hello_str = hello_en()

    else:
        return False

    return '_'.join(hello_str for _ in range(rep))
