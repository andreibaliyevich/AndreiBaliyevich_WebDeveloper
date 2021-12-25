from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import translation
from abaliyevich.celery import app


@app.task
def send_contact_to_email(language_code, form_cd):
    """ Send contact to email """
    prev_language_code = translation.get_language()
    translation.activate(language_code)

    context = {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_HOST': settings.SITE_HOST,
        'form_name': form_cd['name'],
        'form_email': form_cd['email'],
        'form_content': form_cd['content'],
    }

    subject = render_to_string('email/contact_to_email_subject.txt', context)
    text_content = render_to_string('email/contact_to_email_text.html', context)
    html_content = render_to_string('email/contact_to_email.html', context)

    email = EmailMultiAlternatives(
        subject,
        text_content,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_RECEIVER],
    )
    email.attach_alternative(html_content, 'text/html')
    email.send(fail_silently=False)

    translation.activate(prev_language_code)
