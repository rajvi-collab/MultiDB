"""Users urls."""
from .views import ProductHomeView
from django.conf.urls import url

urlpatterns = [
    url(r'^product/$', ProductHomeView.as_view(), name='product'),
    url(r'^details/(?P<id>\d+)/(?P<data>[\w-]+)/$', ProductHomeView.as_view(), name='product_detail'),
]
