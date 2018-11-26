from celery import shared_task

from django.core.mail import send_mail
from django.http import HttpResponse

@shared_task
def send(subject, message, from_email, to_emails, html_template):
	send_mail(
		subject,
		message,
		from_email,
		to_emails,
		html_message=html_template,
		fail_silently=False,
	)
