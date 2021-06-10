from django.shortcuts import render
from datetime import datetime, timedelta

import py_web_ui.bootstrap as bootstrap
import request.ui as ui

import resources.utility as utility


def weekly_request(request):

    today = datetime.now()
    date = today + timedelta(days=7)

    body_html = [ ui.page_title() ]
    body_html.append(ui.week_title(date))

    body_html.append(ui.name_field())
    for day in utility.week_list(date):
        body_html.append(ui.day_of_week_form(day))

    body_html.append(ui.submit_button())

    body_html = bootstrap.container('\n'.join(body_html), fluid=True)

    return render(request, 'index.html', { 'body_html': body_html})
