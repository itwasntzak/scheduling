from django.urls import path

import request.views as views

urlpatterns = [
    path('', view=views.weekly_request, name='weekly-request'),
    path(
        route='receive_weekly_request',
        view=views.receive_weekly_request,
        name='receive-weekly-request'
    ),
]
