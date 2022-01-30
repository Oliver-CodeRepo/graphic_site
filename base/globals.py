
from email.message import EmailMessage
import threading

from django.template.loader import render_to_string

from Graphics import settings



def send_html_email(to_list, subject, template_name, context, sender=settings.DEFAULT_FROM_EMAIL):
    """
    """
    try:
        msg_html = render_to_string(template_name, context)
        msg = EmailMessage(subject=subject, body=msg_html, from_email=sender, bcc=to_list)
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
        print('was sent inside: ', msg)
        return True
    except Exception as e:
        return False