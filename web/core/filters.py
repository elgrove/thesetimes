from datetime import datetime


def print_date(dtobj):
    """Jinja2 filter for printing dates with a st/nd/rd/th suffix."""
    mapping = {"1": "st", "2": "th", "3": "rd"}
    try:
        suffix = mapping[str(dtobj.day)[-1]]
    except KeyError:
        suffix = "th"

    print_format = f"%H:%M, %-d{suffix} %B"
    return datetime.strftime(dtobj, print_format)
