from pathlib import Path


def write_emails_to_markdown(emails, output_path: str) -> None:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    parts = ["# Newsletter Digest\n"]

    # Calculate overall time range from valid datetime objects
    datetimes = [e.get("datetime_obj") for e in emails if e.get("datetime_obj")]

    if datetimes:
        min_dt = min(datetimes)
        max_dt = max(datetimes)
        time_range = f"{min_dt.strftime('%Y-%m-%d %I:%M %p')} → {max_dt.strftime('%Y-%m-%d %I:%M %p')}"
        parts.append(f"**Time Range:** {time_range}\n")

    parts.append("\n")

    if not emails:
        parts.append("_No emails found._\n")
    else:
        for idx, item in enumerate(emails, start=1):
            parts.append(f"## Email {idx}\n")
            parts.append(f"**Source:** {item['source']}\n")
            parts.append(f"**Date:** {item['date']}\n")
            parts.append(f"**Subject:** {item['subject']}\n")
            parts.append("\n### Content\n")
            parts.append(f"{item['content']}\n")
            parts.append("\n---\n")

    Path(output_path).write_text("\n".join(parts), encoding="utf-8")