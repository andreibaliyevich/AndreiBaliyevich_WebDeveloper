from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Project


class PortfolioView(ListView):
    """ Portfolio page """
    model = Project
    paginate_by = 9
    template_name = 'portfolio/portfolio.html'


class ProjectDetailView(DetailView):
    """ Project Detail page """
    model = Project
    template_name = 'portfolio/project_detail.html'
