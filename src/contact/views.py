from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from .forms import MessageForm
from .services import check_recaptcha
from .tasks import send_contact_to_email


def contact(request):
    """ Contact page """
    if request.method == 'POST':
        message_form = MessageForm(request.POST)

        if check_recaptcha(request):
            if message_form.is_valid():
                message_form.save()
                send_contact_to_email.delay(
                    request.LANGUAGE_CODE, message_form.cleaned_data)
                messages.success(request, _('Your message has been sent!'))
                return redirect('contact:contact')
        else:
            messages.error(request, _('Invalid reCAPTCHA. Please try again.'))
    else:
        message_form = MessageForm()

    context = {
        'message_form': message_form,
        'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
    }
    return render(request, 'contact/contact.html', context)
