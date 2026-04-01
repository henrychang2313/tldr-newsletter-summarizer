import imaplib # lib allows you to access and manipulate emails in a mailbox
import email
from email.header import decode_header
from datetime import datetime, timedelta

from config import GMAIL_EMAIL, GMAIL_PASSWORD, TLDR_EMAIL, OUTPUT_MARKDOWN
from parser import choose_best_text
from markdown_writer import write_emails_to_markdown
from cleaner import clean_newsletter_text


def decode_mine_words(s):
    decoded = decode_header(s)
    return "".join(
        [
        part.decode(encoding or "utf-8") if isinstance(part, bytes) else part for part, encoding in decoded
        ]
    )

def extract_email_body(msg):
    plain_text = ""
    html_text = ""

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition", ""))

            if "attachment" in content_disposition:
                continue
            
            payload = part.get_payload(decode=True)
            if not payload:
                continue
            
            charset = part.get_content_charset()

            try:
                decoded_payload = payload.decode(charset or "utf-8", errors="replace")
            except:
                decoded_payload = payload.decode("utf-8", errors="replace")
            
            if content_type == "text/plain":
                plain_text += decoded_payload
            elif content_type == "text/html":
                html_text += decoded_payload
    else:
        content_type = msg.get_content_type()
        payload = msg.get_payload(decode=True)

        if not payload:
            charset = msg.get_content_charset()
            try:
                decoded_payload = payload.decode(charset or "utf-8", errors="replace")
            except:
                decoded_payload = payload.decode("utf-8", errors="replace")

            if content_type == "text/plain":
                plain_text += decoded_payload
            elif content_type == "text/html":
                html_text += decoded_payload
    return plain_text, html_text
    

def fetch_emails_from_sender(sender_email, days_back=1):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(GMAIL_EMAIL,GMAIL_PASSWORD)
    mail.select("inbox")

    since_date = (datetime.now() - timedelta(days=days_back)).strftime("%d-%b-%Y")

    status, messages = mail.search(
        None,
        f'FROM "{sender_email}" SINCE "{since_date}"'
    )

    if status != "OK":
        print("Error searching in inbox")
        return []

    email_ids = messages[0].split()

    results = []

    for eid in email_ids:
        status, msg_data = mail.fetch(eid, "(RFC822)")
        if status != "OK":
            continue
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        subject = decode_mine_words(msg.get("Subject"))
        sender = decode_mine_words(msg.get("From"))

        data_raw = msg.get("Date", "")
        dt = None
        formatted_date = data_raw

        try:
            dt = parsedate_to_datetime(data_raw)
            if dt:
                formatted_date = dt.strftime("%Y-%m-%d %I:%M %p")
        except:
            pass

        plain_text, html_text = extract_email_body(msg)
        content = choose_best_text(plain_text, html_text)
        content = clean_newsletter_text(content)

        if len(content.strip())<120:
            continue

        results.append({
            "subject": subject,
            "sender": sender,
            "date": formatted_date,
            "datetime_obj": dt,
            "content":content,
        })

    mail.logout()
    return results

if __name__ == "__main__":
    emails = fetch_emails_from_sender(TLDR_EMAIL)

    markdown_ready_emails = [
        {
            "source":e["sender"],
            "date":e["date"],
            "datetime_obj":e["datetime_obj"],
            "subject":e["subject"],
            "content":e["content"],

        }
        for e in emails
    ]

    write_emails_to_markdown(markdown_ready_emails, OUTPUT_MARKDOWN)
    print(f"Found {len(emails)} cleaned emails.")
    print(f"Markdwn written to: {OUTPUT_MARKDOWN}")

    