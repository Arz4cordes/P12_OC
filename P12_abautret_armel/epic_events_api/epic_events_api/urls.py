"""epic_events_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from epic_events_api import views as api_views

cli_router = routers.SimpleRouter()
cli_router.register('client', api_views.ClientViewSet, basename='client')

ctr_router = routers.SimpleRouter()
ctr_router.register('contract', api_views.ContractViewSet, basename='contract')

evt_router = routers.SimpleRouter()
evt_router.register('event', api_views.EventViewSet, basename='event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(cli_router.urls)),
    path('', include(ctr_router.urls)),
    path('', include(evt_router.urls)),
]
