def generate_code(name_bird=""):
    if not isinstance(name_bird, str):
        raise ValueError("ERROR")
    name_bird = name_bird.strip()
    if name_bird == "":
        raise ValueError("ERROR")
    words = name_bird.upper().replace("-", "- ").split()
    if len(words) == 1:
        code = words[0][:4]
    elif len(words) == 2:
        code = words[0][:2] + words[1][:2]
    elif all([len(words) == 3, "-" in words[1], name_bird.count("-") == 1]):
        code = words[0][:2] + words[1][0] + words[2][0]
    elif len(words) == 3:
        code = words[0][0] + words[1][0] + words[2][:2]
    elif len(words) == 4:
        code = words[0][0] + words[1][0] + words[2][0] + words[3][0]
    return code
