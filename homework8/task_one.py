def text_up(func):
    def wrap(*args):
        result = func(*args)
        return result.upper()

    return wrap


@text_up
def get_text(strings):
    result = ' '.join(strings)
    return result


print(get_text(['Hello', 'world']))
