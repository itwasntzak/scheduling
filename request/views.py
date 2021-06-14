from django.shortcuts import redirect, render
from django.urls import reverse
from datetime import datetime, timedelta

import py_web_ui.bootstrap as bootstrap
from request.models import SingleDayRequest
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

    today = datetime.now()
    date = today + timedelta(days=7)
    week = utility.week_list(date)

    if request.method == 'POST':
        monday_info = [
            week[0],
            request.POST.get('mondayAvailability'),
            request.POST.get('mondayNote')
        ]
        tuesday_info = [
            week[1],
            request.POST.get('tuesdayAvailability'),
            request.POST.get('tuesdayNote')
        ]
        wednesday_info = [
            week[2],
            request.POST.get('wednesdayAvailability'),
            request.POST.get('wednesdayNote')
        ]
        thursday_info = [
            week[3],
            request.POST.get('thursdayAvailability'),
            request.POST.get('thursdayNote')
        ]
        friday_info = [
            week[4],
            request.POST.get('fridayAvailability'),
            request.POST.get('fridayNote')
        ]
        saturday_info = [
            week[5],
            request.POST.get('saturdayAvailability'),
            request.POST.get('saturdayNote')
        ]
        sunday_info = [
            week[6],
            request.POST.get('sundayAvailability'),
            request.POST.get('sundayNote')
        ]

        name = request.POST.get('name')

        monday = SingleDayRequest.objects.create(
            date=monday_info[0],
            availability=monday_info[1],
            note=monday_info[2],
            name=name
        )
        tuesday = SingleDayRequest.objects.create(
            date=tuesday_info[0],
            availability=tuesday_info[1],
            note=tuesday_info[2],
            name=name
        )
        wednesday = SingleDayRequest.objects.create(
            date=wednesday_info[0],
            availability=wednesday_info[1],
            note=wednesday_info[2],
            name=name
        )
        thursday = SingleDayRequest.objects.create(
            date=thursday_info[0],
            availability=thursday_info[1],
            note=thursday_info[2],
            name=name
        )
        friday = SingleDayRequest.objects.create(
            date=friday_info[0],
            availability=friday_info[1],
            note=friday_info[2],
            name=name
        )
        saturday = SingleDayRequest.objects.create(
            date=saturday_info[0],
            availability=saturday_info[1],
            note=saturday_info[2],
            name=name
        )
        sunday = SingleDayRequest.objects.create(
            date=sunday_info[0],
            availability=sunday_info[1],
            note=sunday_info[2],
            name=name
        )

    return redirect(reverse('weekly-request'))
