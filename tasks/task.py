def replacer(s: str) -> str:
    """
    Add your code here
    """
    new_s = ''
    for i in s:
        if i == "'":
            new_s += '"'
        elif i == '"':
            new_s += "'"
        else:
            new_s += i
    return new_s

replacer(' abc"jfjf\'jf ')

