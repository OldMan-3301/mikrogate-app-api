from django.urls import path, include
from rest_framework.routers import DefaultRouter

from sales import views


router = DefaultRouter()
router.register('router', views.RouterViewSet)
router.register('antenna', views.AntennaViewSet)
router.register('packages', views.PackageViewSet)
router.register('contracts', views.ContractViewSet)

app_name = 'sales'

urlpatterns = [
    path('', include(router.urls))
]
