from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('experience/', views.ExperienceView.as_view(), name='experience'),

    path('set/language/<str:language_code>/',
        views.set_language,
        name='set_language'),
]
