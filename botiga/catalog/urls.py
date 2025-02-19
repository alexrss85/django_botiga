from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('catalog/', include(router.urls)),
]