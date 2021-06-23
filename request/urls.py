from django.urls import path

import request.views as views

urlpatterns = [
    path('', view=views.weekly_request, name='weekly-request'),
]
