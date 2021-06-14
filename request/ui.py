from django.urls import reverse
from django.middleware.csrf import get_token

import py_web_ui.bootstrap as bootstrap
import py_web_ui.html as html
import py_web_ui.strings as html_strings
import resources.strings as strings
import resources.utility as utility


def submit_button():
    return html.div(
        bootstrap.btn(
            value='Submit',
            form='weeklyRequest',
            type='submit',
            extra_classes='btn-primary'
        ),
        classes='text-center my-4',
    )


def token_field(request):
    return html.input_tag(
        input_type=html_strings.hidden_field_input_type,
        name='csrfmiddlewaretoken',
        value=get_token(request)
    )


def weekly_request_form(week, request):

    fields = [ token_field(request) ]

    for day in week:
        weekday = day.strftime('%A').lower()
        date = day.strftime('%m/%d')
        # label
        label_text = '{}{}{}'.format(weekday.title(), html.br, date)
        label = html.div(
            html.label(
                content=label_text,
                to='{}Form'.format(weekday),
                classes='form-label'
            ),
            classes='col-auto'
        )
        # availability
        shift_options = [
            html.option('any', selected=True),
            html.option('close'), html.option('off'),
            html.option('late'), html.option('late rush'),
            html.option('open'), html.option('rush')
        ]
        availability = html.div(
            html.select(
                options=shift_options,
                name='{}Availability'.format(weekday),
                classes='form-select'
            ),
            classes='col-auto ms-3'
        )
        # note
        note = html.div(
            html.input_tag(
                input_type=html_strings.text_field_input_type,
                name='{}Note'.format(weekday),
                classes='form-control'
            ),
            classes='col'
        )

        fields.append(html.div(
            '\n'.join([label, availability, note]),
            classes='row gx-2 mb-0 mx-2 mx-md-5 align-items-center'
        ))
    # name
    fields.append(name_field())

    return html.form(
        content='\n'.join(fields),
        method='post',
        action=reverse('receive-weekly-request'),
        id='weeklyRequest',
    )


def name_field():
    label = html.div(
        html.label(
            content='Name:',
            to='name',
            classes='col-form-label'
        ),
        classes='col-auto'
        # classes='col-auto col-sm-1'
    )
    html_input = html.div(
            html.input_tag(
                input_type=html_strings.text_field_input_type,
                id='name', name='name',
                classes='form-control',
                required=True
            ),
            classes='col ms-3'
        )

    return bootstrap.row(
        '\n'.join([label, html_input]),
        extra_classes='gx-2 mt-2 mx-2 mx-md-5'
    )


def week_title(date):
    days = utility.week_range(date)
    
    return bootstrap.row(
        bootstrap.col(
            content=html.h5(
                content=strings.week_of.format(
                    days[0].strftime('%m/%d'),
                    days[1].strftime('%m/%d')
                ),
                classes='mt-2 mb-3'),
            size=12,
            extra_classes='text-center'
        )
    )


def page_title():
    return bootstrap.row(
        bootstrap.col(
            content=html.h1(
                content=strings.schedule_request.title().format(html.br),
                classes='mt-4 mb-2'
            ),
            size=12,
            extra_classes='text-center'
        )
    )
