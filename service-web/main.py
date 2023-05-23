import os

from core.app import create_app, start_development_server
from core.blueprint import core
from core.filters import print_date

if __name__ == "__main__":
    start_development_server()
