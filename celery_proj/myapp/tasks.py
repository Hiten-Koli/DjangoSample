from celery import shared_task
from django.core.mail import send_mail
@shared_task
def add(x, y):
    return x + y

@shared_task
def send_welcome_email(user_email):
    subject = "Welcome to MyApp!"
    message = "Thank you for signing up. We are excited to have you!"
    send_mail(subject, message, "noreply@myapp.com", [user_email])
    return f"Email sent to {user_email}"