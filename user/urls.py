from django.urls import path

import user.views as views

urlpatterns = [
    path('login/', view=views.login_view, name='login'),
]
