from django.conf.urls import url, include
from product_app import views
from product_app.views import ProductModelViewSet,UserCreateModelViewSet,TokenModelViewSet,LogInModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('productapi', views.ProductModelViewSet,)

router2 = DefaultRouter()
router2.register('tokenapi', views.TokenModelViewSet,)

router3 = DefaultRouter()
router3.register('userloginapi', views.LogInModelViewSet,basename="userlogin")

router4 = DefaultRouter()
router4.register('usercreateapi', views.UserCreateModelViewSet,basename="usercreateapi")


urlpatterns = [
  url(r'^product/', include('product_app.urls')),
  url(r'^users/', include('smartmin.users.urls')),
  url(r'^api-auth/', include('rest_framework.urls')),
  url(r'productapi/', include(router.urls)),
  url(r'tokenapi/', include(router2.urls)),
  url(r'userloginapi/', LogInModelViewSet.as_view()),
  url(r'usercreateapi/', UserCreateModelViewSet.as_view()),
]
