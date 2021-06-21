from django.db.models import fields
from django.forms import ModelForm

from request.models import ScheduleRequest


class ScheduleRequestForm(ModelForm):
    class Meta:
        model = ScheduleRequest
        fields = [
            'date',
            'availability',
            'note',
            'name'
        ]
