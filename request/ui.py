
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
        classes='text-center my-5',
    )


def day_of_week_form(day):

    weekday = day.strftime('%A').lower()
    date = day.strftime('%m/%d')

    label_text = '{}{}{}'.format(weekday.title(), html.br, date)
    label = html.div(
        html.label(
            content=label_text,
            to='{}Form'.format(weekday),
            classes='form-label'
        ),
        classes='col-auto'
        # classes='col-2 me-4'
    )

    availability_id = '{}Availability'.format(weekday)
    availability = html.div(
        html.input_tag(
            input_type=html_strings.checkbox_field_input_type,
            id=availability_id, name=availability_id,
            classes='form-check-input'
        ),
        classes='col-1 col-sm-auto'
        # classes='col-1'
    )


    shift_options = [
        html.option('any', selected=True),
        html.option('close'),
        html.option('late'),
        html.option('late rush'),
        html.option('open'),
        html.option('rush')
    ]
    preference = html.div(
        html.select(
            options=shift_options,
            id='{}ShiftOption'.format(weekday),
            classes='form-select'
        ),
        classes='col-3 col-sm-2 col-md-1'
        # classes='col-2'
    )

    note = html.div(
        html.input_tag(
            input_type=html_strings.text_field_input_type,
            name='{}Note'.format(weekday),
            classes='form-control'
        ),
        classes='col'
        # classes='col-6'
    )

    form =  html.div(
        '\n'.join([label, availability, preference, note]),
        classes='row gx-2 mb-2 align-items-center'
    )

    return html.form(form, 'post', id='weeklyRequest')


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
                classes='form-control'
            ),
            classes='col'
            # classes='col-11 col-sm-11'
        )

    return bootstrap.row(
        '\n'.join([label, html_input]),
        extra_classes='gx-1 mt-3 mb-3'
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
                classes='my-2'),
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
