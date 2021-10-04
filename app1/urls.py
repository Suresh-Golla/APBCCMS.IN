from django.urls import path

from app1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Register', views.Register, name='Register'),
    path('login', views.login, name='login'),
    path('jobs', views.jobs, name='jobs'),
    path('training', views.training, name='training'),
    path('jobsmela', views.jobsmela, name='jobsmela'),
    path('reports', views.reports, name='reports'),
    path('helpdesk', views.helpdesk, name='helpdesk'),
    path('contacts', views.contacts, name='contacts'),
    path('updates', views.updates, name='updates'),
]