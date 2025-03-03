from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('payments', views.PaymentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]