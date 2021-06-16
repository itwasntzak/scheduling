from django.db.models import fields
from django.forms import ModelForm

from request.models import SingleDayRequest, DurationRequest


class SingleDayRequestForm(ModelForm):
    class Meta:
        model = SingleDayRequest
        fields = [
            'date',
            'availability',
            'note',
            'name'
        ]


class DurationRequest(ModelForm):
    class Meta:
        model = DurationRequest
        fields = [
            'start_date',
            'end_date',
            'name'
        ]
