from datetime import datetime
import json


def print_date(input):
    # takes json date format and returns nicer date format for article pages
    try:
        return datetime.strftime(
            datetime.strptime(input, "%Y-%m-%dT%H:%M:%S"), "%H:%M, %d %B"
        )
    except:
        return datetime.strftime(
            datetime.strptime(input, "%Y-%m-%dT%H:%M:%S.%f"), "%H:%M, %d %B"
        )


def parse_json(data):
    return json.loads(json_util.dumps(data))
