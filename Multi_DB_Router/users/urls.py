"""Users urls."""
from .views import LoginView, HomeView
from django.conf.urls import url


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^details/(?P<id>\d+)/$', HomeView.as_view(), name='user_detail'),
]
