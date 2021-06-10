from django.urls import path

from request.views import weekly_request

urlpatterns = [
    path('', view=weekly_request),
]
