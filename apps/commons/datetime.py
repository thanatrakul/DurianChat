from dateutil.relativedelta import relativedelta
from django.utils.timesince import timesince


def relativedelta_to_dict(delta):
    delta_dict = {
        'years': delta.years,
        'months': delta.months,
        'days': delta.days,
        'hours': delta.hours,
        'minutes': delta.minutes,
        'seconds': delta.seconds
    }
    return delta_dict


def humanize_duration(start_datetime, end_datetime):
    delta = relativedelta(end_datetime, start_datetime)
    duration_humanize = timesince(start_datetime, end_datetime)

    duration_dict = relativedelta_to_dict(delta)
    return duration_dict, duration_humanize
