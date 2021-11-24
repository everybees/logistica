from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

import accounts.views as av

router = DefaultRouter(trailing_slash=False)
app_router = routers.DefaultRouter()
app_router.register('', av.AccountsViewSet, basename='accounts')

urlpatterns = [
    path('', include(app_router.urls)),
]
