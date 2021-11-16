from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name="home"),
    path('activity', views.activity, name="activity"),
    path('sadmin', views.admin, name="sadmin"),
    path('companies', views.companies, name="companies"),
    path('importf', views.importf, name="importf"),
    path('jobs', views.jobs, name="jobs"),
    path('profile', views.profile, name="profile"),
    path('search', views.search, name="search"),
    path('statement', views.statement, name="statement"),
    path('report', views.report, name="report"),
    path('venue_csv', views.venue_csv, name="venue_csv"),
    path('venue_pdf', views.venue_pdf, name="venue_pdf"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('imgages/favicon.ico')))
]
