from django.conf.urls import url
from .views import movies
from rest_framework.authtoken import views as rest_framework_views

namespace_prefix = "api.auth."
urlpatterns = [
    url(r'^movies/$', movies, name='api.movies'),
    ]