from datetime import datetime
import json
from bson import json_util

pub_dict = {
    "nyt": "The New York Times",
    "wsj": "The Wall Street Journal",
    "blb": "Bloomberg",
    "dw": "Deutsche Welle",
    "bbc": "BBC News",
    "ft": "Financial Times",
    "nyr": "The New Yorker",
    'econ': 'The Economist',
    'sky': 'Sky Sports',
    'ars': 'Ars Technica',
    'mit': 'MIT Technology Review'
}


def print_date(input):
    try:
        dtobj = datetime.strptime(input, "%Y-%m-%dT%H:%M:%S")
    except:
        dtobj = datetime.strptime(input, "%Y-%m-%dT%H:%M:%S.%f")
    final_format = ""
    sts = [1, 21, 31]
    nds = [2, 22]
    rds = [3, 23]
    if dtobj.day in sts:
        final_format = "%H:%M, %-dst %B"
    elif dtobj.day in nds:
        final_format = "%H:%M, %-dnd %B"
    elif dtobj.day in rds:
        final_format = "%H:%M, %-drd %B"
    else:
        final_format = "%H:%M, %-dth %B"
    # takes json date format and returns nicer date format for article pages
    return datetime.strftime(dtobj, final_format)


def parse_json(data):
    return json.loads(json_util.dumps(data))
