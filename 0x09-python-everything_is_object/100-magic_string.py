def magic_string():
    if not hasattr(magic_string, 'count'): magic_string.count = 0
    magic_string.count += 1
    return ('Best' + ', Best' * (magic_string.count - 1))
