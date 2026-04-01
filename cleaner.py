import re


BLOCKLIST_PATTERNS = [
    r"unsubscribe",
    r"manage preferences",
    r"view in browser",
    r"privacy policy",
    r"terms of service",
    r"advertisement",
    r"advertiser",
    r"sponsored",
    r"follow us on",
    r"copyright \d{4}",
    r"shop now",
    r"buy now",
    r"free shipping",
    r"click here",
    r"download the app",
    r"sign up",
    r"advertise",
    r"view online",
    r"apply here",
    r"create your own role",
]

NOISY_LINE_HINTS = [
    "http://",
    "https://",
    "instagram",
    "facebook",
    "twitter",
    "linkedin",
    "tiktok",
    "youtube",
    "jobs@",
    "utm_source=",
]

FOOTER_START_PATTERNS = [
    r"^want to advertise",
    r"^want to work at",
    r"^if you have any comments or feedback",
    r"^manage your subscriptions",
    r"^love tldr\?",
    r"^share your referral link",
    r"^track your referrals here",
    r"^links:$",
]

SPONSOR_TRIGGER_PATTERNS = [
    r"\(sponsor\)",
    r"^together with",
]

SECTION_HEADER_PATTERNS = [
    r"^[A-Z0-9 &/:\-'\.\?\!]+$",
]


def strip_invisible_characters(text: str) -> str:
    if not text:
        return ""

    invisible_chars = [
        "\u200b",  # zero width space
        "\u200c",  # zero width non-joiner
        "\u200d",  # zero width joiner
        "\ufeff",  # byte order mark
        "\xa0",    # non-breaking space
    ]

    for ch in invisible_chars:
        text = text.replace(ch, " ")

    return text


def is_section_header(line: str) -> bool:
    line = line.strip()
    if not line:
        return False

    if len(line) > 120:
        return False

    return any(re.match(pattern, line) for pattern in SECTION_HEADER_PATTERNS)


def clean_newsletter_text(text: str) -> str:
    if not text:
        return ""

    text = strip_invisible_characters(text)

    lines = [line.strip() for line in text.splitlines()]
    cleaned_lines = []

    in_sponsor_block = False

    for line in lines:
        if not line:
            continue

        lower = line.lower()

        # Stop entirely when footer / link dump starts
        if any(re.search(pattern, lower) for pattern in FOOTER_START_PATTERNS):
            break

        # Start skipping sponsor block
        if any(re.search(pattern, lower) for pattern in SPONSOR_TRIGGER_PATTERNS):
            in_sponsor_block = True
            continue

        # End sponsor block when next obvious section header starts
        if in_sponsor_block and is_section_header(line):
            in_sponsor_block = False

        if in_sponsor_block:
            continue

        # Remove obvious junk lines
        if any(re.search(pattern, lower) for pattern in BLOCKLIST_PATTERNS):
            continue

        # Skip noisy social / tracking / link-heavy lines
        link_hits = sum(1 for hint in NOISY_LINE_HINTS if hint in lower)
        if link_hits >= 2:
            continue

        # Skip numbered reference links like [1] https://...
        if re.match(r"^\[\d+\]\s+https?://", line):
            continue

        # Skip empty nav/branding fragments
        if line in {"TLDR", "TLDR DATA", "TLDR FINTECH"}:
            continue

        # Skip date-only newsletter header fragments like TLDR 2026-03-30
        if re.match(r"^[A-Z ]+\d{4}-\d{2}-\d{2}$", line):
            continue

        # Skip very short meaningless fragments
        if len(line) < 3:
            continue

        # Skip lines mostly made of punctuation/symbols
        alpha_chars = sum(ch.isalpha() for ch in line)
        if alpha_chars == 0 and len(line) < 20:
            continue

        cleaned_lines.append(line)

    text = "\n".join(cleaned_lines)

    # Collapse excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    return text