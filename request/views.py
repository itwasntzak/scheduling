from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from request.forms import ScheduleRequestForm
from request.models import ScheduleRequest
import resources.utility as utility 


@login_required(
    login_url='/user/login/',
    redirect_field_name=''
)
def weekly_request(request):

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
            form = ScheduleRequestForm(form_data)
            if form.is_valid():
                ScheduleRequest.objects.create(
                    date=form.cleaned_data['date'],
                    availability=form.cleaned_data['availability'],
                    note=form.cleaned_data['note'].lower(),
                    name=form.cleaned_data['name'].lower()
                )
            else:
                print(form.errors)

    week_list = []
    for day in week:
        week_list.append(
            {
                'weekday': day.strftime('%A').lower(),
                'date': day.strftime('%m/%d')
            }
        )

    context = {
        'week': week_list,
        'starting_date': utility.week_range(date)[0].strftime('%m/%d'),
        'ending_date': utility.week_range(date)[-1].strftime('%m/%d'),
    }

    return render(request, 'weekly_request.html', context)
