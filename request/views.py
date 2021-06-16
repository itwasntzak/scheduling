from django.shortcuts import redirect, render
from django.urls import reverse
from datetime import datetime, timedelta

import py_web_ui.bootstrap as bootstrap
from request.forms import SingleDayRequestForm
from request.models import SingleDayRequest
import resources.utility as utility 


def weekly_request(request):

    date = datetime.now() + timedelta(days=7)
    week = []
    for day in utility.week_list(date):
        week.append(
            {
                'weekday': day.strftime('%A').lower(),
                'date': day.strftime('%m/%d')
            }
        )

    context = {
        'week': week,
        'starting_date': utility.week_range(date)[0].strftime('%m/%d'),
        'ending_date': utility.week_range(date)[-1].strftime('%m/%d'),
    }

    return render(request, 'weekly_request.html', context)


def receive_weekly_request(request):

    today = datetime.now()
    date = today + timedelta(days=7)
    week = utility.week_list(date)

    if request.method == 'POST':
        for day in week:
            weekday = day.strftime('%A').lower()
            form_data = {
                'date': day,
                'availability': request.POST.get(f'{ weekday }Availability'),
                'note': request.POST.get(f'{ weekday }Note'),
                'name': request.POST.get('name')
            }
            form = SingleDayRequestForm(form_data)
            if form.is_valid():
                SingleDayRequest.objects.create(
                    date=form.cleaned_data['date'],
                    availability=form.cleaned_data['availability'],
                    note=form.cleaned_data['note'].lower(),
                    name=form.cleaned_data['name'].lower()
                )
            else:
                print(form.errors)

    return redirect(reverse('weekly-request'))
