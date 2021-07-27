from __future__ import absolute_import, unicode_literals

from smtplib import SMTPException
import requests
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from celery.utils.log import get_task_logger
from acmon.celery import app


logger = get_task_logger(__name__)


@app.task
def send_email(mail_subject, message, to, html_message=None):
    """ sends email to emails list """

    msg = EmailMultiAlternatives(
        # title:
        mail_subject,
        # message:
        message,
        # from:
        settings.DEFAULT_FROM_EMAIL,
        # to:
        to
    )
    if html_message:
        msg.attach_alternative(html_message, "text/html")

    try:
        msg.send()
        result = f"Email {mail_subject} sent to {to[0]}"
    except SMTPException as error:
        result = f"Connection error while send email to {error}"

    logger.info(result)
    return result


@app.task
def send_sms(recipients, message):
    """ sends sms to recipient """

    try:
        url = f"{settings.SMS_SERVER_URL}?token={settings.SMS_TOKEN}"
        data = {}
        data['recipients'] = recipients
        data['sms'] = {'sender': settings.SMS_SENDER, 'text':message}

        requests.post(url, json=data)
        result = f"SMS {message} sent to {recipients}"
    except SMTPException as error:
        result = f"Connection error while send email to {error}"

    logger.info(result)
    return result
