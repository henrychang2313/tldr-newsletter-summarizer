from bs4 import BeautifulSoup


def html_to_text(html: str) -> str:
    if not html:
        return ""

    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg", "img"]):
        tag.decompose()

    text = soup.get_text("\n")
    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]

    return "\n".join(lines)


def choose_best_text(plain_text: str, html_text: str) -> str:
    plain_text = (plain_text or "").strip()
    html_text = (html_to_text(html_text) or "").strip()

    if len(html_text) > len(plain_text):
        return html_text
    return plain_text