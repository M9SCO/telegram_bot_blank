from re import escape, sub
from typing import Dict, Any


def multiple_replace(to_change: Dict[str, Any], old_text: str) -> str:
    pattern = "|".join(map(escape, to_change.keys()))
    new_text = sub(pattern, lambda m: str(to_change[m.group()]), old_text)
    return new_text

