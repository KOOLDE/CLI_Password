def is_numeric(string: str) -> bool:
    try:
        int(string)
        return True
    except ValueError:
        return False
