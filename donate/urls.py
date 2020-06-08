from django.urls import path

from .views import donatePageView, charge, successPageView

urlpatterns = [
    path('', donatePageView, name = 'donate'),
    path('charge/', charge, name = 'charge'),
    path('success/', successPageView, name = 'success'),
]