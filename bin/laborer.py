import re

def multiple_replace(dic, text) -> str:
    pattern = "|".join(map(re.escape, dic.keys()))
    return re.sub(pattern, lambda m: dic[m.group()], text)

