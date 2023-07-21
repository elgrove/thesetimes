from core.app import create_app, start_development_server

app_factory = create_app

if __name__ == "__main__":
    start_development_server()
