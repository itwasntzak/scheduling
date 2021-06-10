from django.db.models import fields
from django.forms import ModelForm

from request.models import SingleDayRequest, DurationRequest


class SingleDayRequestForm(ModelForm):
    class Meta:
        model = SingleDayRequest
        fields = [
            'date',
            'availability',
            'shift',
            'note',
            'name'
        ]


class DurationRequest(ModelForm):
    class Meta:
        model = DurationRequest
        fields = [
            'start_time',
            'end_time',
            'name'
        ]
