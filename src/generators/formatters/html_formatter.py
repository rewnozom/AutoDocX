def format_html(doc_content):
    """
    Formaterar dokumentationen till HTML-format.
    Placeholder: Returnerar innehållet omslutet av <p>-taggar.
    """
    return f"<p>{doc_content}</p>"

if __name__ == "__main__":
    sample = "Exempel på dokumentation."
    print("HTML format:", format_html(sample))
