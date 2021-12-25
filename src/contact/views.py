from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView
from .models import Message
from .tasks import send_contact_to_email


class ContactView(SuccessMessageMixin, CreateView):
    """ Contact page """
    model = Message
    fields = ['name', 'email', 'content']
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact:contact')
    success_message = _('Your message has been sent!')

    def form_valid(self, form):
        send_contact_to_email.delay(
            self.request.LANGUAGE_CODE, form.cleaned_data)
        return super().form_valid(form)
