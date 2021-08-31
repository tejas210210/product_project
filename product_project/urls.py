from django.conf.urls import url, include
from product_app.views import *


urlpatterns = [
  url(r'^product/', include('product_app.urls')),
  url(r'^users/', include('smartmin.users.urls')),
]
