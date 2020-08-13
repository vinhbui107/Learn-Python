from datetime import datetime
import requests
import sys

from formatting import format_msg
from send_email import send_email


def send(name, website=None, to_email=None, verbose=False):

    if website != None:
        msg = format_msg(name=name)
    else:
        msg = format_msg(name=name, website=website)
    if verbose:
        print(name, website, to_email)
    # send the message

    try:
        send_email(text=msg, to_emails=[to_email], html=None)
        send = True
    except:
        send = False

    return send


if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]
    response = send(name, to_email=email, verbose=True)
    print(response)
