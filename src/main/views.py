from django.conf import settings
from django.shortcuts import render, redirect
from django.utils.translation import activate
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    """ Home page """
    template_name = 'main/index.html'


class AboutView(TemplateView):
    """ About page """
    template_name = 'main/about.html'


class ExperienceView(TemplateView):
    """ Experience page """
    template_name = 'main/experience.html'


def set_language(request, language_code):
    """ Set language """
    languages_dict = dict(settings.LANGUAGES)
    if languages_dict.get(language_code, None):
        activate(language_code)
    return redirect('main:index')


def error_400(request, exception):
    """ Error 400 """
    return render(request, 'errors/400.html', status=400)


def error_403(request, exception):
    """ Error 403 """
    return render(request, 'errors/403.html', status=403)


def error_404(request, exception):
    """ Error 404 """
    return render(request, 'errors/404.html', status=404)


def error_500(request):
    """ Error 500 """
    return render(request, 'errors/500.html', status=500)
