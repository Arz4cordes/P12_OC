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
from api_use import views as client_views
from api_contract import views as contract_views
from api_event import views as event_views
from connection import views as connect_views

client_router = routers.SimpleRouter()
client_router.register('client', client_views.ClientViewSet, basename='client')

contract_router = routers.SimpleRouter()
contract_router.register('contract', contract_views.ContractViewSet, basename='contract')

evt_router = routers.SimpleRouter()
evt_router.register('event', event_views.EventViewSet, basename='event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('home/', connect_views.HomeAPIView.as_view(), name='home'),
    path('', include(client_router.urls)),
    path('', include(contract_router.urls)),
    path('', include(evt_router.urls)),
]
