# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# username and password of account sending email
username = "btvinh107@gmail.com"
password = "SieunhanGG1999"


def send_email(
    text="Email body",
    subject="Hello World",
    from_email="Hungry Py <hungrypy@gmail.com>",
    to_emails=None,
    html=None,
):
    assert isinstance(to_emails, list)

    msg = MIMEMultipart("alternative")
    msg["From"] = from_email
    msg["To"] = ", ".join(to_emails)
    msg["Subject"] = subject
    txt_part = MIMEText(text, "plain")
    msg.attach(txt_part)
    if html != None:
        html_part = MIMEText(html, "html")
        msg.attach(html_part)
    msg_str = msg.as_string()

    # login to my smtp server
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()