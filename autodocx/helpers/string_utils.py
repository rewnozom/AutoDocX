# src/helpers/string_utils.py
def trim(text):
    """
    Tar bort överflödiga blanktecken i början och slutet av texten.
    """
    return text.strip()


def to_upper(text):
    """
    Konverterar texten till versaler.
    """
    return text.upper()


def to_lower(text):
    """
    Konverterar texten till gemener.
    """
    return text.lower()


def replace_substring(text, old, new):
    """
    Ersätter alla förekomster av 'old' med 'new' i texten.
    """
    return text.replace(old, new)


if __name__ == "__main__":
    sample = "   Hej, världen!   "
    print("Original:", repr(sample))
    print("Trim:", repr(trim(sample)))
    print("Upper:", to_upper(sample))
    print("Lower:", to_lower(sample))
    print("Replace:", replace_substring(sample, "världen", "World"))
