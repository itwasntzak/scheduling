from django.shortcuts import redirect, render
from django.urls import reverse
from datetime import datetime, timedelta

import py_web_ui.bootstrap as bootstrap
import request.ui as ui
import resources.utility as utility 


def weekly_request(request):

    today = datetime.now()
    date = today + timedelta(days=7)

    body_html = [ ui.page_title() ]
    body_html.append(ui.week_title(date))

    body_html.append(ui.weekly_request_form(utility.week_list(date), request))

    body_html.append(ui.submit_button())

    body_html = bootstrap.container('\n'.join(body_html), fluid=True)

    return render(request, 'index.html', { 'body_html': body_html })


def receive_weekly_request(request):

    if request.method == 'POST':
        print(request.POST)

    return redirect(reverse('weekly-request'))
