msg_template = """ Hello {name}
Thank you for joining {website}. We are very
happy to have you with us.
"""


def format_msg(name="Vinh", website="shit.com"):
    my_msg = msg_template.format(name, website)
    return my_msg
